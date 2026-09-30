# Stage 2A — Raw Dataset Curation Reanalysis
Version: rana_dataset_v002
Source: barunya.zip, 34 image files.

## Curation principle
No role assignment is inherited merely because a similar coverage category was discussed previously. Each source row is tied to an actual filename and visual inspection.

## Actual raw-set findings
- 34 image files total.
- Most original camera images are 3:4 portrait photographs; several smaller portrait exports are also present.
- Repeated frontal portrait sequence with neutral, smile, frown, wink/playful, pout, eyes-closed, looking-up and looking-down expressions.
- Full-body front, 3/4, side and rear examples are present.
- Sitting examples are present.
- Indoor and outdoor examples are present.
- Multiple hijab colors/styles are present, including black, white/light neutral, pink, taupe/olive-taupe and pashmina-style draping.
- Clothing varies enough to test wardrobe disentanglement.

## Dataset rules
- Preserve original filenames as immutable source identifiers.
- Do not bake hijab or clothing into the identity token.
- Avoid over-weighting near-identical consecutive portrait frames.
- Preserve view diversity.
- Keep rear/side/full-body evidence available for evaluation.
- Use validation/holdout to test unseen combinations rather than simply repeating training compositions.
