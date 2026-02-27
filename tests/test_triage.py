from project_alpha.triage import Priority, classify_call


def test_critical_for_explicit_self_harm_language() -> None:
    result = classify_call("I want to end my life. I feel hopeless.")
    assert result.priority == Priority.CRITICAL
    assert result.score >= 8


def test_high_for_crisis_signals_without_explicit_lethality() -> None:
    result = classify_call("I had a panic attack and severe anxiety after abuse.")
    assert result.priority == Priority.HIGH


def test_medium_for_moderate_distress() -> None:
    result = classify_call("I am stressed and cannot sleep these days.")
    assert result.priority == Priority.MEDIUM


def test_low_for_empty_transcript() -> None:
    result = classify_call("   ")
    assert result.priority == Priority.LOW
    assert "No usable transcript" in result.reasons[0]
