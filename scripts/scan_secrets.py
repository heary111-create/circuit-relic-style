#!/usr/bin/env python3
"""Limited working-directory credential scan. Never print matched values."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re

SKIP_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', 'dist', 'build'}
SKIP_SUFFIXES = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.pdf', '.zip', '.7z',
                 '.rar', '.mp4', '.mov', '.mp3', '.wav'}
MAX_BYTES = 2_000_000
PATTERNS = [
    ('API key pattern', re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b')),
    ('GitHub token', re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b')),
    ('GitHub fine-grained token', re.compile(r'\bgithub_pat_[A-Za-z0-9_]{20,}\b')),
    ('AWS access key', re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b')),
    ('Private key block', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----')),
    ('Likely hard-coded secret assignment', re.compile(
        r'''(?ix)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key|client[_-]?secret|
        password|passwd|auth[_-]?token)\b["']?\s*[:=]\s*["'](?P<value>[^"'\r\n]{12,})["']''')),
]
SAFE_VALUES = {'YOUR_API_KEY_HERE', '<REDACTED_SECRET>', 'REDACTED', 'PLACEHOLDER', 'EXAMPLE_ONLY'}


def scan_text(text: str) -> list[tuple[str, int]]:
    findings = []
    for label, pattern in PATTERNS:
        for match in pattern.finditer(text):
            value = match.groupdict().get('value')
            if value in SAFE_VALUES:
                continue
            findings.append((label, text.count('\n', 0, match.start()) + 1))
    return findings


def scan(root: Path) -> tuple[list, list, int, int]:
    findings, errors = [], []
    scanned = skipped = 0

    def traversal_error(error):
        # Exception strings can contain private absolute paths.
        errors.append(('directory traversal', type(error).__name__))

    for directory, dirs, files in os.walk(root, followlinks=False, onerror=traversal_error):
        kept = [name for name in dirs
                if name not in SKIP_DIRS and not (Path(directory) / name).is_symlink()]
        skipped += len(dirs) - len(kept)
        dirs[:] = kept
        for name in sorted(files):
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            try:
                if path.is_symlink() or path.suffix.lower() in SKIP_SUFFIXES:
                    skipped += 1
                    continue
                with path.open('rb') as stream:
                    data = stream.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES or b'\x00' in data:
                    skipped += 1
                    continue
                try:
                    content = data.decode('utf-8-sig')
                except UnicodeDecodeError:
                    skipped += 1
                    continue
                scanned += 1
                findings.extend((rel, label, line) for label, line in scan_text(content))
            except OSError as error:
                errors.append((rel, type(error).__name__))
    return findings, errors, scanned, skipped


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.')
    args = parser.parse_args(argv)
    try:
        root = Path(args.root).resolve(strict=True)
        if not root.is_dir():
            raise NotADirectoryError
    except (OSError, ValueError):
        print('Scan error: root must be an accessible directory.')
        return 2

    findings, errors, scanned, skipped = scan(root)
    for rel, label, line in findings:
        print(f'{rel}:{line} [{label}] [REDACTED]')
    for rel, category in errors:
        print(f'Scan error: {rel} [{category}]')
    print(f'Scanned {scanned} text files; skipped {skipped} files/directories.')
    if errors:
        print('Scan incomplete; resolve errors before relying on this check.')
        return 2
    if findings:
        print('Potential credentials detected. Review privately and rotate real exposed credentials.')
        return 1
    print('No supported credential patterns detected in scanned files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
