# Project Alpha: AI Triage for Mental Health Telecalling

Project Alpha is an AI-assisted classification system designed to help mental-health telecalling services (e.g., Tele-MANAS, iCALL) prioritize large volumes of caller transcripts.

## What is implemented now
This repository now includes an executable MVP triage classifier:
- Keyword-weight based scoring model (`critical`, `high`, `medium`, `low`).
- Transparent reasoning output (matched phrases + score impact).
- CLI for quick local use.
- Unit tests for core triage behavior.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Classify a transcript:
```bash
project-alpha-triage "I feel hopeless and I want to end my life"
```

Example output:
```text
priority=critical
confidence=0.98
score=12
reasons=
- Matched phrase: 'end my life' (+8)
- Matched phrase: 'hopeless' (+4)
```

## Safety note
This tool is for **human-in-the-loop decision support only**. It must not be used as a fully autonomous clinical decision system.

## Planned next steps
1. Replace keyword logic with calibrated ML/NLP models.
2. Add multilingual handling and ASR integration.
3. Add fairness checks and cohort-level performance reports.
4. Integrate with queue management workflows.
