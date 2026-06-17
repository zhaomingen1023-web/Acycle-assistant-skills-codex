# Acycle Workflows

## Use This Reference When

Read this file when the user asks which Acycle path to use, how to move from raw series to analysis, or how to translate a scientific question into an Acycle workflow.

## Core Task Map

### Import and inspect

Use this path when the user has not yet standardized the data.

- Verify that the independent variable is monotonic.
- Prefer two numeric columns for the first pass.
- Record units before any interpolation or tuning discussion.
- Flag irregular spacing early because many downstream steps depend on it.

### Prepare and resample

Use this path when spacing is irregular, files come from spreadsheets, or multiple columns need cleanup.

- Convert to a simple text table.
- Remove or document missing values.
- Decide whether resampling or interpolation is scientifically justified.
- Keep the original file and the Acycle-ready derived file separate.

### Spectral analysis

Use this path when the user wants dominant periodicities in a series that can reasonably be treated as stationary over the analyzed interval.

Good fit:

- “What are the main cycles in this depth series?”
- “Do I see orbital-scale periodicity?”
- “Which peaks are strongest after detrending?”

Watch for:

- overinterpreting peaks from short series
- unreported detrending choices
- period ranges that exceed what the record length can resolve

### Evolutionary spectrum or wavelet-style inspection

Use this path when cyclicity changes with depth or time.

Good fit:

- “When does the cycle strengthen or weaken?”
- “Does the dominant period drift?”
- “Is the cyclic structure transient?”

Watch for:

- window-size tradeoffs
- boundary effects
- interpreting visually strong patterns without significance context

### Correlation, tuning, and astrochronology

Use this path when the user wants orbital tuning, sedimentation-rate reasoning, or target matching.

Good fit:

- “Can I tune this record to orbital targets?”
- “What sedimentation-rate range makes the spectrum plausible?”
- “How do I compare this to expected eccentricity or precession bands?”

Require the user or downstream analysis to document:

- the chosen target series
- the age or depth anchors
- assumptions behind sedimentation rate
- how sensitive the result is to alternate settings

### COCO or eCOCO-style interpretation

Use this path when the user is evaluating accumulation or sedimentation-rate scenarios from spectral structure.

Treat outputs as model-supported hypotheses, not direct proof. Always ask:

- what tuning or target assumptions enter the workflow
- whether independent constraints support the preferred rate
- whether alternative rates produce similarly plausible alignments

## Response Template

When mapping a user request to Acycle, prefer this compact structure:

1. State the scientific goal.
2. State the data condition that matters most.
3. Recommend the Acycle workflow category.
4. List the parameters that need a human decision.
5. List the minimum QA checks before interpretation.

## Example Mappings

- Raw CSV with depth and isotope values:
  prepare a two-column file, inspect spacing, then consider interpolation and spectral analysis.
- Already detrended but irregularly spaced record:
  review whether the detrending happened before or after interpolation, then choose a stationary or evolutionary workflow.
- Wants “astronomical tuning” with no target specified:
  pause and ask for the target framework or make explicit that the workflow cannot be defended without one.
