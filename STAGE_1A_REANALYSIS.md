# Stage 1A — Identity Specification Reanalysis from Raw Data
Version: rana_identity_v002
Source: barunya.zip — 34 image files inspected from original pixels.

## Ground truth
This revision supersedes earlier memory-based coverage summaries. Stable and variable attributes are derived from the supplied raw images; user-provided physical reference values remain separate metadata.

## Stable identity observations
- Adult woman; the collection consistently depicts the same adult subject.
- Facial identity is represented by a dense frontal portrait sequence plus 3/4 and side views.
- Body identity is represented by repeated full-body front, 3/4, side and rear views.
- Head-to-body proportion and body silhouette should be preserved rather than normalized to a generic model.
- Natural skin and lighting variation should not become identity drift.
- Apparent adult age is stable across the collection.

## User-provided physical metadata
- Height reference: 155 cm
- Weight reference: 53 kg

## Identity-locked
- facial structure and identity
- head/body proportion
- body silhouette and relative proportions
- apparent adult age
- natural rendering characteristics

## Variable
- hijab style, color and tying arrangement
- clothing
- pose
- expression
- environment
- lighting
- camera/framing

## Important finding
Multiple hijab families and colors occur while the same subject identity recurs. Hijab must remain a conditioning variable, not part of rana_person identity.

## Separation rule
rana_person = identity
hijab = variable
clothing = variable
pose = variable
expression = variable
environment = variable
lighting = variable
camera = variable

Only visible properties from the supplied pixels are treated as evidence. Ambiguous attributes must be marked for review rather than filled from memory.
