# Circuit Relic Style

**Preserve the shape. Replace the material.**

[简体中文](README.md) · [Examples](examples.md) · [Contributing](CONTRIBUTING.md) · [MIT License](LICENSE)

Circuit Relic Style is a portable image style skill that reconstructs a reference image as PCB artwork. Preserve the subject's silhouette, pose and composition while rebuilding its materials with turquoise circuit boards, copper traces, silver solder joints, chips and restrained red conductive accents.

Version: **1.1.1**. This repository contains prompts, style instructions and maintenance scripts. It does not contain model weights or an image generation engine. The main skill instructions are in Chinese; the master prompt is in English.

## Quick start

1. Supply your reference image to an image editor that supports image input.
2. Copy [the master prompt](prompts/master_prompt.txt) and replace `[SUBJECT_DESCRIPTION]`, `[POSE_DESCRIPTION]` and `[ICONIC_ELEMENTS]`.
3. Optionally use [the negative prompt](prompts/negative_prompt.txt). If your host has no separate negative field, include the relevant exclusions in the main prompt.
4. Specify any background, palette, board shape or aspect-ratio overrides. Check recognition at a distance and circuit detail close up.

For agent use, place the complete `circuit-relic-style/` folder in your host's documented skill location and reload as required. The entry point is [SKILL.md](SKILL.md). Hosts supporting explicit skill invocation may use:

```text
Use $circuit-relic-style to transform this reference image.
Preserve its silhouette, pose and composition. Use a black outer background.
```

`agents/openai.yaml` supplies optional UI metadata. `manifest.json` is project-specific descriptive metadata, not a universal plugin manifest. Installation paths and invocation behavior depend on your host; cross-host end-to-end testing has not been performed.

## Behavior and limits

- Default: a complete rectangular PCB with four gold-plated corner mounting holes and a black outer background.
- User instructions override background, palette, shape and viewpoint defaults.
- Preserve the reference orientation, subject count, pose and iconic structures.
- A text-only host can prepare prompts; actual images require an image generation/editing tool.
- Transparent output requires host support and a verified alpha channel.
- The skill needs no credentials of its own. Image providers may require authentication, credits or payment.
- Hardware realism is visual art direction, not a claim of electrical function or manufacturability.
- [Examples](examples.md) are written scenarios, not verified before/after image results.

See [the visual specification](STYLE_SPEC.md), [analysis template](templates/reference_analysis.md), [security policy](SECURITY.md), [contribution guide](CONTRIBUTING.md), [publishing guide](docs/PUBLISHING.md) and [changelog](CHANGELOG.md).

## Validation

Python 3.10+ and the standard library are sufficient:

```bash
python scripts/validate_repo.py
python scripts/scan_secrets.py .
python -m unittest discover -s tests -v
```

GitHub Actions runs these checks on pushes and pull requests. The scanner checks supported patterns in the working directory, not Git history, text inside images, or all credential types.

## License

Original repository prompts, documentation and scripts use the [MIT License](LICENSE). Retain copyright and license notices when redistributing. Reference images, third-party assets and generated outputs are subject to their own applicable rights and provider terms. See [Choose a License](https://choosealicense.com/licenses/mit/) for an overview of MIT permissions.
