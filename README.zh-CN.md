# Acycle-assistant-skills-codex

这是一个面向 Codex 的非官方 Acycle 辅助 skill 打包仓库，用于数据预处理、分析流程规划，以及结果的谨慎解释与写作辅助。

English version: [README.md](README.md)

## 仓库概览

这个仓库里的 skill 主要帮助你完成：

- 将原始表格数据整理成适合 Acycle 使用的两列序列文件
- 规划 Acycle 中的频谱分析、演化分析与调谐类工作流
- 将 Acycle 的处理步骤和结果整理成更适合论文方法或结果部分的表述

这个 skill 是 Acycle 工作流的辅助工具，不包含 Acycle 软件本体，也不会声称自己能够直接在 Acycle 图形界面里代替用户点击操作。

## 仓库结构

```text
Acycle-assistant-skills-codex/
  README.md
  README.zh-CN.md
  LICENSE
  NOTICE
  skills/
    acycle-assistant/
      SKILL.md
      manifest.json
      VERSION
      agents/openai.yaml
      references/
      scripts/
```

## 安装方式

可以直接使用 Codex 的 skill 安装脚本从 GitHub 安装：

```powershell
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" `
  --repo zhaomingen1023-web/Acycle-assistant-skills-codex `
  --path skills/acycle-assistant
```

也可以通过仓库 URL 安装：

```powershell
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" `
  --url https://github.com/zhaomingen1023-web/Acycle-assistant-skills-codex/tree/main/skills/acycle-assistant
```

安装完成后，建议重启 Codex，这样新 skill 会在后续会话中被正确发现。

## 使用示例

- `Use $acycle-assistant to prepare my CSV for Acycle.`
- `Use $acycle-assistant to suggest an Acycle spectral analysis workflow.`
- `Use $acycle-assistant to summarize these Acycle results in methods-ready language.`

## 范围说明

本仓库包含：

- skill 元数据与路由说明
- Acycle 工作流选择与结果解释的参考文档
- 一个将原始表格整理成 Acycle 可用序列文件的辅助脚本

本仓库不包含：

- Acycle 软件本体或源码
- Acycle 手册、截图或第三方打包资源
- 任何“官方 Acycle 发布物”的暗示

## 署名与说明

本仓库是非官方辅助 skill。Acycle 软件本身由 Mingsong Li 及其合作者开发。若你 fork、转载或再次发布本仓库，请保留“非官方辅助工具”的说明。
