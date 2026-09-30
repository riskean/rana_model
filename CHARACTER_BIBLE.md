# CHARACTER BIBLE — rana_person

## Identity

Canonical identity token: `rana_person`

Subject: adult woman.

User-provided physical metadata:
- height: 155 cm
- weight: 53 kg

## Identity-locked attributes

- facial identity and proportions
- head-to-body proportion
- observed body silhouette and relative proportions
- natural skin/rendering characteristics
- apparent adult age consistency
- expression behavior when an expression preset is explicitly requested

## Variable attributes

- hijab presence/style/color/tie
- square hijab / pashmina variants
- clothing
- shoes/accessories
- makeup
- pose
- expression
- environment
- lighting
- camera/framing

## Hard rule

Hijab is wardrobe, not identity.

Never create identity tokens such as:
- `rana_black_hijab`
- `rana_white_hijab`
- `rana_pashmina`

## Truth hierarchy

Original pixels > explicit user metadata > documented observation > engineering assumption.

Unverified attributes must remain unspecified.

## Realism rules

Do not automatically:
- beautify
- smooth skin into plastic texture
- enlarge eyes/lips
- change apparent age
- change body proportions
- enlarge/reduce the head
- introduce generic AI facial features

The goal is faithful photographic identity, not an idealized replacement face.
