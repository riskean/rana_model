"""Validate public conditioning metadata without accessing private image binaries."""

import csv
from pathlib import Path

REQUIRED = {
    "asset_id", "source_filename", "asset_kind", "role", "split",
    "status", "preprocess_note", "asset_filename", "asset_sha256",
    "dimensions", "mask_filename", "mask_sha256",
}

def validate(path: str) -> list[str]:
    errors = []
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
    if not rows:
        return ["manifest is empty"]
    if set(rows[0]) != REQUIRED:
        errors.append("unexpected manifest columns")
    if len(rows) != 18:
        errors.append(f"expected 18 records, found {len(rows)}")
    if any(r["split"] != "train" for r in rows):
        errors.append("conditioning baseline contains non-TRAIN assets")
    if any(r["status"] != "PASS" for r in rows):
        errors.append("conditioning manifest contains non-PASS assets")
    kinds = {k: sum(r["asset_kind"] == k for r in rows) for k in ("identity","expression","body")}
    if kinds != {"identity":4, "expression":9, "body":5}:
        errors.append(f"unexpected asset counts: {kinds}")
    masks = sum(bool(r["mask_filename"]) for r in rows)
    if masks != 13:
        errors.append(f"expected 13 facial masks, found {masks}")
    return errors

if __name__ == "__main__":
    errors = validate("CONDITIONING_ASSET_MANIFEST_v002.csv")
    if errors:
        raise SystemExit("\n".join(errors))
    print("conditioning manifest: PASS")
