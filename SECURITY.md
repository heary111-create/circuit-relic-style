# Security & Privacy

## Scope

Circuit Relic Style itself requires no API key or account credentials. Image tools supplied by the host may have their own authentication, billing and data-processing requirements. Use the host's authorized mechanisms; do not place credentials in this repository or in prompts.

For style-transfer tasks, process only the reference image and instructions supplied for the task. Do not inspect unrelated files or credential stores. Do not include secrets, machine-specific absolute paths or source-image location metadata in public examples. These instructions are behavioral guidance, not a sandbox or an automatic metadata-removal tool.

## Reporting a vulnerability

When the repository has GitHub private vulnerability reporting enabled, use **Security → Advisories → Report a vulnerability**. Include the affected version, a redacted reproduction and the impact. Do not post working credentials, private files or exploitable details in a public Issue.

If private reporting is unavailable and no private maintainer contact is published, open an Issue asking for a private contact channel without disclosing the vulnerability details. This repository does not promise a response deadline. Security fixes target the latest published version; older releases are not separately maintained.

Maintainers can enable the feature following [GitHub's private reporting guide](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).

## Local scan

```bash
python scripts/scan_secrets.py .
```

The dependency-free scanner detects a limited set of credential patterns in UTF-8 text files up to 2 MB. It prints only relative paths, line numbers and finding categories; it never prints matched credential values. Exit code 0 means no supported patterns were found, 1 means possible credentials were found, and 2 means the scan could not complete (for example an invalid root or unreadable file).

It skips Git internals, common dependency/build folders, symlinks, known media/archive formats, binary files and files above the size limit. Skipped counts are reported. It does not scan Git history, archives, image metadata or text in screenshots, and is not an exhaustive secret detector. A pass does not certify that a repository is safe to publish. `.gitignore` also does not remove files already tracked in Git.

## If a credential is exposed

Revoke or rotate it through the provider, remove the value from the working tree, and assess affected Git history, releases, logs and copies. Merely deleting the newest copy does not invalidate the credential. Avoid reproducing the value while reporting or fixing the issue.
