#!/usr/bin/env python3
"""Validate this repository's versions, declared resources and local Markdown links."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote


def validate(root):
    errors = []
    required = ['SKILL.md', 'README.md', 'README.en.md', 'LICENSE', 'CHANGELOG.md',
                'CONTRIBUTING.md', 'SECURITY.md', 'manifest.json', 'agents/openai.yaml',
                'scripts/scan_secrets.py', 'tests/test_scan_secrets.py',
                '.github/workflows/secret-scan.yml', 'docs/PUBLISHING.md']
    for name in required:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    if errors:
        return errors
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    name, version = manifest['name'], manifest['version']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('Invalid skill name')
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        errors.append('Invalid release version')
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    if not match:
        errors.append('Missing skill frontmatter')
    else:
        front = match.group(1)
        keys = set(re.findall(r'^([a-z_-]+):', front, re.M))
        if not {'name', 'description'} <= keys:
            errors.append('Missing skill name/description')
        if keys - {'name', 'description', 'license', 'metadata', 'allowed-tools'}:
            errors.append('Unsupported skill frontmatter keys')
        if f'name: {name}\n' not in front or f'version: "{version}"' not in front:
            errors.append('Skill and manifest name/version mismatch')
        if 'license: MIT' not in front or manifest.get('license') != 'MIT':
            errors.append('License metadata mismatch')
    for filename in ['README.md', 'README.en.md']:
        if f'**{version}**' not in (root / filename).read_text(encoding='utf-8'):
            errors.append(f'Version missing in {filename}')
    if f'## {version}\n' not in (root / 'CHANGELOG.md').read_text(encoding='utf-8'):
        errors.append('Current version missing from changelog')
    declared = [manifest['entrypoint'], *manifest['files'].values(),
                manifest['security']['secret_policy'], manifest['security']['secret_scan']]
    for rel in declared:
        path = (root / rel).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append(f'Missing or unsafe manifest resource: {rel}')
    for path in root.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            if re.match(r'^[a-z]+:', target, re.I) or target.startswith('#'):
                continue
            rel = unquote(target.split('#', 1)[0])
            dest = (path.parent / rel).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f'Broken local link: {path.relative_to(root)} -> {target}')
    master = (root / manifest['files']['master_prompt']).read_text(encoding='utf-8')
    expected = {'SUBJECT_DESCRIPTION', 'POSE_DESCRIPTION', 'ICONIC_ELEMENTS'}
    if set(re.findall(r'\[([A-Z_]+)\]', master)) != expected:
        errors.append('Master prompt variables differ from documented inputs')
    if len((root / 'LICENSE').read_text(encoding='utf-8')) < 1000:
        errors.append('License text appears incomplete')
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    try:
        errors = validate(root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Repository validation could not complete: {type(error).__name__}')
        return 2
    for error in errors:
        print(error)
    if errors:
        return 1
    print('Repository validation passed: versions, metadata, resources and local links.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
