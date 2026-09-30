from rana_harness.resolver import resolve_prompt

def test_identity_only():
    r = resolve_prompt("rana_person")
    assert r.identity == "rana_person" and r.expression == "neutral"
    assert r.wardrobe == () and r.identity_reference == "neutral_front"

def test_smile_and_hijab_are_separate():
    r = resolve_prompt("rana_person, smiling, black square hijab")
    assert r.expression == "smiling"
    assert r.expression_preset == "smiling"
    assert r.wardrobe == ("black square hijab",)
    assert r.identity == "rana_person"

def test_view_does_not_change_identity():
    r = resolve_prompt("rana_person, three_quarter, white square hijab, pose:standing")
    assert r.identity == "rana_person"
    assert r.view == "three_quarter"
    assert r.identity_reference == "neutral_three_quarter"
    assert r.pose == "standing"

def test_missing_identity_is_rejected():
    try:
        resolve_prompt("smiling, black square hijab")
    except ValueError:
        return
    assert False
