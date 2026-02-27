from __future__ import annotations

import argparse

from .triage import classify_call


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="project-alpha-triage",
        description="Classify a mental-health call transcript into triage priority.",
    )
    parser.add_argument(
        "transcript",
        nargs="?",
        help="Transcript text to classify. If omitted, input is read from stdin.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    transcript = args.transcript
    if transcript is None:
        transcript = input().strip()

    result = classify_call(transcript)

    print(f"priority={result.priority.value}")
    print(f"confidence={result.confidence}")
    print(f"score={result.score}")
    print("reasons=")
    for reason in result.reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()
