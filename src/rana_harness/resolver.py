"""Deterministic prompt/conditioning resolver for rana_person.

No model weights or personal image data are embedded here.
"""
from dataclasses import dataclass, asdict
from typing import Optional

IDENTITY_TOKEN = "rana_person"
EXPRESSIONS = {"neutral", "smiling", "pout", "wink_smile", "eyes_closed", "looking_up", "looking_down"}
VIEWS = {"front", "three_quarter", "side", "rear"}

@dataclass(frozen=True)
class ConditioningRequest:
    identity: str
    expression: str
    wardrobe: tuple[str, ...]
    pose: Optional[str]
    view: str
    environment: Optional[str]
    lighting: Optional[str]
    camera: Optional[str]
    identity_reference: str
    expression_preset: Optional[str]

def _tokens(prompt: str) -> list[str]:
    return [t.strip() for t in prompt.split(",") if t.strip()]

def resolve_prompt(prompt: str) -> ConditioningRequest:
    toks = _tokens(prompt)
    if IDENTITY_TOKEN not in toks:
        raise ValueError("Prompt must contain the canonical identity token 'rana_person'.")
    expr = "neutral"
    view = "front"
    pose = environment = lighting = camera = None
    wardrobe = []
    for token in toks:
        if token in EXPRESSIONS:
            expr = token
        elif token in VIEWS:
            view = token
        elif token.startswith("pose:"):
            pose = token.split(":", 1)[1].strip() or None
        elif token.startswith("environment:"):
            environment = token.split(":", 1)[1].strip() or None
        elif token.startswith("lighting:"):
            lighting = token.split(":", 1)[1].strip() or None
        elif token.startswith("camera:"):
            camera = token.split(":", 1)[1].strip() or None
        elif token != IDENTITY_TOKEN:
            wardrobe.append(token)
    return ConditioningRequest(
        identity=IDENTITY_TOKEN,
        expression=expr,
        wardrobe=tuple(wardrobe),
        pose=pose,
        view=view,
        environment=environment,
        lighting=lighting,
        camera=camera,
        identity_reference="neutral_front" if view == "front" else "neutral_three_quarter",
        expression_preset=None if expr == "neutral" else expr,
    )

def resolve_dict(prompt: str) -> dict:
    return asdict(resolve_prompt(prompt))
