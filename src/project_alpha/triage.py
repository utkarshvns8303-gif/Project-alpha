from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class Priority(str, Enum):
    """Priority bands used by telecalling services."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass(frozen=True)
class TriageResult:
    priority: Priority
    confidence: float
    score: int
    reasons: list[str]


KEYWORD_WEIGHTS: dict[str, int] = {
    "suicide": 8,
    "kill myself": 8,
    "end my life": 8,
    "self harm": 7,
    "can't go on": 6,
    "overdose": 6,
    "hurt someone": 7,
    "panic attack": 4,
    "abuse": 4,
    "violent": 5,
    "hopeless": 4,
    "severe anxiety": 4,
    "depressed": 3,
    "can't sleep": 2,
    "stressed": 2,
    "worried": 1,
    "lonely": 1,
    "follow up": 0,
}


def _matched_keywords(text: str, keywords: Iterable[str]) -> list[str]:
    lowered = text.lower()
    return [kw for kw in keywords if kw in lowered]


CRITICAL_PHRASES = {"suicide", "kill myself", "end my life", "self harm", "overdose", "hurt someone"}


def _score_to_priority(score: int, matched: list[str]) -> Priority:
    if any(phrase in CRITICAL_PHRASES for phrase in matched):
        return Priority.CRITICAL
    if score >= 7:
        return Priority.HIGH
    if score >= 2:
        return Priority.MEDIUM
    return Priority.LOW


def _confidence_for(score: int, matched_count: int) -> float:
    base = min(0.35 + score * 0.07, 0.95)
    boost = min(matched_count * 0.03, 0.12)
    return round(min(base + boost, 0.98), 2)


def classify_call(transcript: str) -> TriageResult:
    """Classify a call transcript into a priority band.

    This MVP classifier intentionally uses a transparent keyword-weight model.
    It is meant for human-in-the-loop triage assistance, not autonomous decisions.
    """

    if not transcript or not transcript.strip():
        return TriageResult(
            priority=Priority.LOW,
            confidence=0.35,
            score=0,
            reasons=["No usable transcript content provided."],
        )

    matched = _matched_keywords(transcript, KEYWORD_WEIGHTS.keys())
    score = sum(KEYWORD_WEIGHTS[kw] for kw in matched)

    if not matched:
        reasons = ["No high-signal risk phrases matched."]
    else:
        reasons = [f"Matched phrase: '{kw}' (+{KEYWORD_WEIGHTS[kw]})" for kw in matched]

    return TriageResult(
        priority=_score_to_priority(score, matched),
        confidence=_confidence_for(score, len(matched)),
        score=score,
        reasons=reasons,
    )
