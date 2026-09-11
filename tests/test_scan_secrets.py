"""Regression tests use synthetic values assembled at runtime, never real credentials."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'scan_secrets.py'
SPEC = importlib.util.spec_from_file_location('scanner', MODULE_PATH)
scanner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scanner)


class ScannerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_scan(self, root=None):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = scanner.main([str(root or self.root)])
        return code, output.getvalue()

    def test_detects_without_logging_value(self):
        value = 'sk-' + 'a' * 24
        (self.root / 'example.txt').write_text('header\n' + value, encoding='utf-8')
        code, output = self.run_scan()
        self.assertEqual(code, 1)
        self.assertIn('example.txt:2', output)
        self.assertNotIn(value, output)
        self.assertNotIn(str(self.root), output)

    def test_supported_provider_patterns(self):
        samples = ['ghp_' + 'a' * 30, 'github_pat_' + 'b' * 30,
                   'AKIA' + 'A' * 16,
                   '-----BEGIN ' + 'ENCRYPTED PRIVATE KEY-----']
        for value in samples:
            with self.subTest(value_type=value[:4]):
                self.assertTrue(scanner.scan_text(value))

    def test_quoted_json_assignment(self):
        value = 'synthetic-value-for-test'
        self.assertTrue(scanner.scan_text('"password": "' + value + '"'))

    def test_exact_placeholder_allowed(self):
        self.assertFalse(scanner.scan_text('api_key = "' + 'YOUR_API_KEY_HERE' + '"'))

    def test_placeholder_substring_does_not_suppress_secret(self):
        value = 'sk-' + 'EXAMPLE_ONLY' + 'b' * 24
        self.assertTrue(scanner.scan_text(value))

    def test_invalid_root_fails(self):
        code, output = self.run_scan(self.root / 'missing')
        self.assertEqual(code, 2)
        self.assertNotIn('No supported', output)

    def test_read_failure_fails_closed(self):
        (self.root / 'blocked.txt').write_text('safe', encoding='utf-8')
        with patch.object(Path, 'open', side_effect=PermissionError):
            code, output = self.run_scan()
        self.assertEqual(code, 2)
        self.assertIn('Scan incomplete', output)

    def test_binary_oversized_and_git_skipped(self):
        value = ('sk-' + 'a' * 24).encode()
        (self.root / '.git').mkdir()
        (self.root / '.git' / 'ignored').write_bytes(value)
        (self.root / 'binary.dat').write_bytes(b'\x00' + value)
        (self.root / 'large.txt').write_bytes(b'a' * (scanner.MAX_BYTES + 1) + value)
        code, output = self.run_scan()
        self.assertEqual(code, 0)
        self.assertIn('skipped 3', output)

    def test_bom_text_is_scanned(self):
        value = 'sk-' + 'c' * 24
        (self.root / 'bom.txt').write_text(value, encoding='utf-8-sig')
        self.assertEqual(self.run_scan()[0], 1)

    def test_clean_repository(self):
        (self.root / 'readme.md').write_text('PCB artwork', encoding='utf-8')
        self.assertEqual(self.run_scan()[0], 0)


if __name__ == '__main__':
    unittest.main()
