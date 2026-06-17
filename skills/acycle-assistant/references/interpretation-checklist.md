# Interpretation Checklist

## Use This Reference When

Read this file when the user asks for help interpreting Acycle output, defending a workflow, troubleshooting strange results, or writing methods and results sections.

## Preprocessing Checklist

- State the original file format and the derived analysis file format.
- State the independent variable, dependent variable, and units.
- State whether spacing was uniform or irregular before preprocessing.
- State whether interpolation was applied and at what step size.
- State whether detrending was applied and why.
- State how missing values, duplicate x-values, and obvious outliers were handled.

## Analysis Checklist

- State the analysis goal in one sentence.
- State whether the workflow assumes stationary or nonstationary cyclicity.
- State the tested frequency or period range.
- State the significance or comparison framing if used.
- State any external target series, tuning anchors, or sedimentation-rate assumptions.

## Interpretation Guardrails

- Do not treat a single sharp peak as sufficient evidence without record-length context.
- Do not hide preprocessing choices that materially affect periodicities.
- Do not describe tuning results as unique unless sensitivity checks support that claim.
- Do not convert visually appealing banding into a strong claim without discussing edge effects and windowing choices.
- Do not mix depth-domain and time-domain language casually.

## Troubleshooting Patterns

### Peak locations look unstable

Check:

- interpolation step size
- record length
- detrending choice
- whether the period range is too aggressive for the data span

### Too many peaks appear significant

Check:

- whether red-noise or null-model framing was appropriate
- whether preprocessing amplified noise
- whether duplicate or irregular spacing artifacts remain

### Evolutionary map looks visually strong but hard to defend

Check:

- window length and overlap choices
- edge effects
- whether the pattern persists across plausible settings

### Tuning result looks impressive but fragile

Check:

- sensitivity to alternate anchors
- sensitivity to alternate target bands
- whether independent geologic constraints support the preferred solution

## Methods Drafting Checklist

When writing manuscript text, include:

- data source and variable definitions
- preprocessing order
- interpolation settings
- detrending settings
- analysis class used in Acycle
- significance framing
- the criteria used to interpret peaks or tuned solutions

## Results Drafting Checklist

Prefer language like:

- “The analysis is consistent with...”
- “A prominent peak occurs near... under the chosen preprocessing settings.”
- “The tuned solution remains sensitive to...”
- “These patterns support, but do not uniquely prove...”
