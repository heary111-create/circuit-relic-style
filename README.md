# Circuit Relic Style

**保形换质，让参考图由电路本身构成。**

[English](README.en.md) · [使用示例](examples.md) · [贡献指南](CONTRIBUTING.md) · [MIT License](LICENSE)

Circuit Relic Style（电路遗物风格）是一个可移植的图像风格提示词 skill：保留人物、物体或场景的轮廓、姿态、构图，把材质重构为青绿色 PCB、铜走线、银色焊点、芯片与克制的红色导电结构。

当前版本：**1.1.1**。本仓库包含提示词、风格规范与维护脚本，不包含模型权重或独立图像生成程序。

## 视觉原则

- **保留辨识度**：主体数量、轮廓、姿态、方向与构图优先。
- **材质整体重构**：皮肤、衣物、树木、水面和建筑均转译为电子结构。
- **硬件摄影质感**：真实焊点反光、清晰铜走线、安装孔与细密元件。
- **密度形成主体**：通过线路密度与方向组织形体，避免仅叠加电路纹理。
- **克制用色**：青绿与深蓝为基础，银色结构、金色细节和局部深红焦点。

这是视觉艺术方向，不是电路设计工具；输出不代表可制造或可工作的 PCB。

## 快速开始

### 直接使用提示词

1. 在支持参考图编辑的图像工具里上传你的参考图。
2. 复制 [主提示词](prompts/master_prompt.txt)，替换 `[SUBJECT_DESCRIPTION]`、`[POSE_DESCRIPTION]`、`[ICONIC_ELEMENTS]`。
3. 可选：在工具的负面提示词字段中加入 [负面提示词](prompts/negative_prompt.txt)；没有该字段时，将关键排除项写进普通提示词。
4. 补充所需背景、画幅与配色。按“远看辨识主体、中看电子结构、近看硬件细节”检查结果。

完整填写示例见 [examples.md](examples.md)。本仓库提供文字示例，尚未附带经验证的参考图与生成结果对照。

### 作为 agent skill 使用

下载仓库或解压发布包，保持 `circuit-relic-style/` 文件夹结构完整。将整个目录放入宿主规定的 skill 目录，按宿主说明重新加载。入口为根目录的 [SKILL.md](SKILL.md)，不要只复制该文件而丢失 prompts 和其他引用文件。

支持 `$skill-name` 调用的宿主可使用：

```text
使用 $circuit-relic-style 转换这张参考图。
保留主体姿态、翅膀数量和横向构图，黑色背景，红色只用于中心标志物。
```

`agents/openai.yaml` 提供可选的 UI 元数据；`manifest.json` 是本项目的描述性元数据，不是通用插件安装协议。各宿主的目录、触发方式和工具能力可能不同；本发布包未做逐平台端到端验证。

## 能力与默认行为

| 情况 | 行为 |
| --- | --- |
| 有图像编辑工具和参考图 | 使用参考图约束主体、姿态和构图 |
| 只有文本能力 | 输出可复制提示词，不声称已经生成图片 |
| 默认输出 | 完整矩形 PCB、四角金色安装孔、黑色外围背景 |
| 用户指定背景、形状或配色 | 用户要求优先于默认风格设置 |
| 透明背景 | 取决于宿主能力，需要验证文件实际 alpha 通道 |
| 凭据与费用 | skill 本身不需要密钥；宿主或图像服务可能需要登录、额度或付费 |

## 文件导航

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 主工作流与元素转译规则 |
| [STYLE_SPEC.md](STYLE_SPEC.md) | 视觉规范 |
| [prompts/master_prompt.txt](prompts/master_prompt.txt) | 主提示词的唯一维护来源 |
| [prompts/negative_prompt.txt](prompts/negative_prompt.txt) | 默认排除项 |
| [templates/reference_analysis.md](templates/reference_analysis.md) | 参考图分析模板 |
| [examples.md](examples.md) | 请求示例、完整提示词和检查重点 |
| [manifest.json](manifest.json) | 项目版本及资源索引 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 提交改进的方法 |
| [SECURITY.md](SECURITY.md) | 安全范围、扫描限制与问题报告 |
| [docs/PUBLISHING.md](docs/PUBLISHING.md) | GitHub 上传与 Release 步骤 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变化 |

## 本地检查

使用 Python 3.10 或更新版本，无需安装第三方依赖。在仓库根目录运行（Windows 可按环境改用 `py -3`）：

```bash
python scripts/validate_repo.py
python scripts/scan_secrets.py .
python -m unittest discover -s tests -v
```

GitHub Actions 会在 push 和 pull request 时执行相同检查。扫描器只检测当前目录内支持的模式，不覆盖 Git 历史、图片中的文字或全部凭据类型，详见 [SECURITY.md](SECURITY.md)。

## 开源许可

本仓库的原创提示词、文档与脚本使用 [MIT License](LICENSE)，允许使用、修改、分发和商用，并须保留版权与许可声明。参考图、第三方素材与宿主生成结果的权利或使用条款需另行确认，不因本仓库许可自动获得授权。许可说明参考 [GitHub Choose a License](https://choosealicense.com/licenses/mit/)。

欢迎通过 Issue 提供可复现的问题，或通过 Pull Request 改进提示词、文档和示例。项目目前以中文 skill 指令为主，提供英文主提示词和英文 README。
