---
name: acycle-assistant
description: Guide Acycle software workflows for cyclostratigraphy, paleoenvironmental time-series analysis, and reproducible preprocessing. Use when Codex needs to help with Acycle data import, tabular series cleanup, interpolation, detrending, spectral analysis, evolutionary spectral analysis, wavelet or coherence work, astrochronologic tuning, COCO or eCOCO-style interpretation, or conversion of CSV/XLSX/TXT tables into Acycle-ready two-column series files.
---

# Acycle Assistant

## Overview

Help the user prepare stratigraphic or time-series data for Acycle, choose a defensible analysis path, and summarize results in methods-ready language. Treat Acycle as GUI-first software: provide click-by-click guidance, data preparation, parameter planning, and interpretation support, but never claim to have clicked inside the app unless direct evidence is available.

## Quick Start

1. Inspect the user's data layout, units, spacing, and missing values before suggesting any Acycle menu path.
2. Run `scripts/prepare_acycle_series.py` when the input arrives as CSV, TSV, TXT, or spreadsheet-exported text that needs to become a clean two-column series.
3. Read `references/acycle-workflows.md` when the user asks which Acycle workflow or module to use.
4. Read `references/interpretation-checklist.md` when the user asks how to justify settings, assess significance, troubleshoot suspicious peaks, or write methods and results.

## Workflow Decision Tree

- Need import help or file cleanup:
  prepare an Acycle-ready two-column file, confirm monotonic ordering, and give exact import guidance.
- Need periodicity in a roughly stationary series:
  recommend interpolation and detrending checks, then guide the user toward spectral analysis.
- Need frequency changes through depth or time:
  guide the user toward evolutionary spectral analysis or wavelet-style inspection.
- Need orbital tuning, sedimentation-rate reasoning, or target matching:
  guide the user through tuning-oriented workflows and require explicit documentation of assumptions.
- Need manuscript-ready reporting:
  extract preprocessing steps, parameter choices, significance assumptions, and caveats into concise prose.

## Standard Operating Pattern

### 1. Normalize the data model

Treat the first column as the independent variable and the second column as the measured signal unless the user provides a different mapping. Confirm:

- column names and units
- whether the series is depth-domain or time-domain
- whether sampling is uniform or irregular
- whether duplicate x-values, gaps, or obvious outliers exist

If the mapping is ambiguous, state the assumption you use. Do not silently swap columns.

### 2. Prepare an Acycle-ready file

Prefer a plain text file with two numeric columns and no hidden spreadsheet formatting. Use the bundled script when needed:

```powershell
python "$HOME/.codex/skills/acycle-assistant/scripts/prepare_acycle_series.py" `
  --input data.csv `
  --output data_acycle.txt `
  --x depth_m `
  --y d18o `
  --sort `
  --deduplicate average
```

After preparation, report:

- number of rows retained
- rows skipped or repaired
- whether sorting or duplicate handling changed the file
- final x range and approximate spacing

### 3. Choose the analysis path conservatively

Do not jump straight to interpretation. First describe the preprocessing logic:

- whether interpolation is required
- whether detrending is justified
- what frequency or period range is physically meaningful
- what null model or significance framing is being assumed

If the user only asks for “run Acycle,” slow down and make the workflow explicit.

### 4. Give GUI guidance that is easy to follow

When explaining Acycle operations:

- name the task, then the expected input shape
- list the menu or workflow sequence step by step
- call out the parameters the user must decide
- separate recommended defaults from project-specific choices

If you are uncertain about an exact menu name, say that you are inferring from standard Acycle workflows rather than pretending certainty.

### 5. Interpret outputs carefully

Treat peaks, banding, tuning solutions, and sedimentation-rate inferences as conditional. Always connect interpretation to:

- sample spacing and interpolation choices
- detrending choices
- significance settings
- expected orbital or climatic targets
- alternative explanations and edge cases

## Output Style

Prefer one of these response shapes depending on the request:

- `Preparation note`: cleaned file summary plus next Acycle steps
- `Workflow plan`: recommended Acycle path with parameter decisions
- `Interpretation memo`: what the output suggests, what it does not prove, and what to verify next
- `Methods draft`: manuscript-ready preprocessing and analysis prose

## Resource Routing

- Read `references/acycle-workflows.md` for task-to-workflow mapping, common Acycle task categories, and menu-level guidance.
- Read `references/interpretation-checklist.md` for QA, significance framing, manuscript reporting, and troubleshooting.
- Use `scripts/prepare_acycle_series.py` for deterministic cleanup of tabular data into two-column Acycle-ready files.
