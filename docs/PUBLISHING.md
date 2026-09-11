# GitHub 发布指南

本地发布包版本为 **1.1.1**。以下步骤由仓库所有者执行；准备本包并不代表已经创建公开仓库或发布 Release。

## 仓库资料

- 建议仓库名：`circuit-relic-style`
- Description：`Preserve shape, replace material: a portable prompt skill for photorealistic PCB circuit-board artwork.`
- Topics：`agent-skill`、`prompt-engineering`、`image-generation`、`style-transfer`、`pcb`、`generative-art`
- 许可证：MIT，正文见根目录 `LICENSE`。当前署名为 `Circuit Relic Style contributors`，未推断作者真实姓名；需要个人署名时可改成你的公开姓名或署名。
- 首次发布标题：`Circuit Relic Style v1.1.1`
- Release 说明可直接使用 [RELEASE_NOTES_v1.1.1.md](RELEASE_NOTES_v1.1.1.md)。

## 上传文件

1. 解压发布 ZIP，进入 `circuit-relic-style` 目录。`README.md`、`LICENSE`、`SKILL.md` 和 `.github/` 应直接位于仓库根目录，而不是再套一层文件夹。
2. 在 GitHub 创建一个空仓库，准备好后选择 Public；不要让 GitHub 再生成一套 README 或许可证。
3. 在此目录运行检查：

```bash
python scripts/validate_repo.py
python scripts/scan_secrets.py .
python -m unittest discover -s tests -v
```

4. 首次建立本地 Git 仓库：

```bash
git init -b main
git add .
git diff --cached --stat
git commit -m "Prepare Circuit Relic Style v1.1.1"
```

5. 复制新仓库页面给出的实际远程地址，执行页面提示的 `git remote add origin ...` 与 `git push -u origin main`。不要把 ZIP 本身作为仓库唯一文件上传，务必包含 `.github` 等隐藏文件。
6. 查看 Actions 是否通过。本地检查通过不等于 GitHub CI 已经运行成功。

## Release

上传并确认 Actions 通过后，创建标签并推送：

```bash
git tag v1.1.1
git push origin v1.1.1
```

在 GitHub Releases 为 `v1.1.1` 创建发布条目，粘贴发布说明，并可附上已核验的 ZIP。若上传前修改了包内文件，重新打包并计算校验和，避免 Release 源码与附件内容不一致。

建议开启私密漏洞报告；操作见 [GitHub 官方指南](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository)。许可证的展示方式见 [GitHub 许可证说明](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)。

## 后续版本

统一更新 `SKILL.md` 中的 `metadata.version`、`manifest.json`、两份 README 和 `CHANGELOG.md`；新版本添加对应的 Release 说明。视觉展示图可在实际生成并确认公开权限后追加，本包未把虚构示例当作实测作品。
