# Contributing / 贡献指南

欢迎改进 PCB 材质转译、结构保留、提示词兼容性、使用示例与文档翻译。

## 提交问题

使用 Issue 模板，提供版本号、宿主/图像工具及模型、脱敏后的请求、期望结果和实际结果。图片仅在你有权公开时附上。安全问题按 [SECURITY.md](SECURITY.md) 私下报告。

## 提交 Pull Request

1. Fork 仓库，创建描述改动用途的分支。
2. 尽量一次解决一个问题，说明触发条件与修改后的行为。
3. 主提示词只维护在 `prompts/master_prompt.txt`，不要把另一份完整副本放进 `SKILL.md`。
4. 提示词改动应附可复现请求及观察结果；没有运行图像生成时直接注明，不把预期效果写成实测结果。
5. 文档变更保持中文与英文 README 的核心信息一致；涉及行为变更时更新 changelog。
6. 修改扫描器时补充或更新相关回归测试，并运行以下检查。

```bash
python scripts/validate_repo.py
python scripts/scan_secrets.py .
python -m unittest discover -s tests -v
```

维护脚本要求 Python 3.10+，使用标准库。GitHub Actions 执行同样检查。人工图像评审重点：主体数量、姿态与方向、标志物数量、PCB 材质、背景要求、真实透明通道（若适用）。

## 内容与许可

请只提交有权贡献的内容，并同意将自己的贡献按本项目 [MIT License](LICENSE) 分发。不要提交密钥、私人参考图、模型权重或没有明确再分发权限的第三方素材。

保持讨论友善、具体，围绕可复现的行为与视觉证据提供反馈。发布版本由维护者统一更新，不要求每个 PR 都修改版本号。
