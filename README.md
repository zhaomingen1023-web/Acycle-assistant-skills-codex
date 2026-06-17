# Acycle-assistant-skills-codex

Unofficial Codex skill packaging for Acycle-oriented data preparation, workflow planning, and conservative interpretation support.

中文说明见 [README.zh-CN.md](README.zh-CN.md).

## Overview

This repository packages a Codex skill that helps with:

- converting raw tabular data into Acycle-ready two-column series files
- planning Acycle workflows for spectral, evolutionary, and tuning-oriented analysis
- drafting cautious methods and interpretation notes for Acycle outputs

The skill is designed as a companion for Acycle workflows. It does not include the Acycle software itself and does not automate GUI clicking inside Acycle.

## Repository Layout

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

## Install

Install directly from GitHub with the Codex skill installer:

```powershell
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" `
  --repo zhaomingen1023-web/Acycle-assistant-skills-codex `
  --path skills/acycle-assistant
```

Or install from a repo URL:

```powershell
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" `
  --url https://github.com/zhaomingen1023-web/Acycle-assistant-skills-codex/tree/main/skills/acycle-assistant
```

Restart Codex after installation so the skill is discovered in new sessions.

## Example Prompts

- `Use $acycle-assistant to prepare my CSV for Acycle.`
- `Use $acycle-assistant to suggest an Acycle spectral analysis workflow.`
- `Use $acycle-assistant to summarize these Acycle results in methods-ready language.`

## Scope

Included:

- skill metadata and routing instructions
- reference notes for Acycle workflow selection and interpretation QA
- a helper script for preparing Acycle-ready series files

Not included:

- Acycle binaries or source code
- Acycle manuals, screenshots, or bundled third-party assets
- any claim of official affiliation with Acycle

## Attribution and Status

This repository is an unofficial helper skill. Acycle is separate software developed by Mingsong Li and collaborators. If you fork or redistribute this repository, preserve the non-affiliation statement.
