# Prompt Schema

## Canonical order
rana_person, [pose], [view/framing], [expression], [hijab], [clothing], [environment], [lighting], [camera/look]

## Rules
- rana_person means identity only.
- smiling resolves to the subject-specific smile preset.
- Hijab never becomes part of the identity token.
- Clothing never becomes part of the identity token.
- Avoid generic beauty modifiers that alter the observed face.
- Avoid prompts that imply a different age or body structure.
