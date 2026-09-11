# Changelog

## 1.1.1
- Added MIT license, bilingual README, contribution and publishing guides, Issue and PR templates.
- Normalized skill frontmatter and version metadata; added optional agent UI metadata.
- Removed residual named-weapon instructions from the standalone master prompt.
- Linked canonical prompt files instead of embedding duplicate copies in SKILL.md.
- Clarified user overrides, host image capabilities, transparency verification and visual-only PCB realism.
- Fixed secret scanner logging of matched values; added explicit error handling and regression tests.
- Added repository validation to CI; reconciled conflicting color/material examples.


## 1.1.0
- Added zero-secret security and privacy boundary
- Added `SECURITY.md`
- Added GitHub-safe `.gitignore`
- Added dependency-free local secret scanner
- Added GitHub Actions secret scan on push / pull request
- Explicitly forbids reading or exposing local/account credentials
- Explicitly avoids publishing absolute local paths and source-image EXIF/location metadata

## 1.0.1
- 移除朗基奴斯枪专用识别规则
- 红色长矛、叉、刀剑、武器等统一按通用“红色标志物规则”处理
- 保留“保形换质”与主体轮廓、姿态、构图优先原则

## 1.0.0
- 正式命名为 Circuit Relic Style
- 固化“保形换质”原则
- 增加主体 / 姿态 / 构图 / 标志物的优先级规则
- 增加人物、场景、翅膀、披风、树木、山体、水面等转译逻辑
- 增加红色标志物规则
- 增加透明背景输出规则
- 增加标准 Master Prompt 与 Negative Prompt
