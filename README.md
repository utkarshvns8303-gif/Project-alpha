# Project Alpha: AI Triage for Mental Health Telecalling

## Overview
Project Alpha is an AI-assisted classification system designed to help mental health telecalling services (e.g., Tele-MANAS, iCALL) prioritize large volumes of user calls. The system assigns urgency levels to incoming calls so that high-risk callers receive faster attention while maintaining fairness, privacy, and transparency.

## Goals
- **Improve response times** for high-priority callers.
- **Support counselors** with decision aids, not replace them.
- **Operate safely** within clinical and regulatory constraints.
- **Respect privacy** and data minimization principles.

## Target Use Cases
- Incoming call queue triage based on urgency.
- Post-call review to verify triage accuracy.
- Analytics for staffing and resource planning.

## Proposed Priority Levels
1. **Critical** – Immediate risk of harm (self-harm, harm to others).
2. **High** – Severe distress, active crisis, or recent trauma.
3. **Medium** – Moderate distress, needs timely support.
4. **Low** – General counseling or follow-up needs.

## MVP Scope
- **Input**: Call transcripts (real-time or post-call), optional metadata (time, region, previous calls).
- **Output**: Priority label + confidence score + rationale highlights.
- **Human-in-the-loop**: Counselor confirmation required before final action.

## System Design (High-Level)
```
Caller -> Transcript (ASR) -> NLP Classifier -> Priority + Rationale -> Queue Manager
```

### Components
- **ASR**: Converts audio to text (local or managed provider).
- **NLP Classifier**: Fine-tuned transformer or rule+ML hybrid.
- **Rationale Extractor**: Highlights phrases driving urgency.
- **Queue Manager**: Sorts and assigns calls to counselors.

## Model Options
- **Baseline**: Logistic regression / SVM on TF-IDF.
- **Advanced**: DistilBERT / RoBERTa fine-tuned on labeled data.
- **Hybrid**: Rules for critical risk terms + ML for nuance.

## Data & Labeling
- **Training Data**: Historical call transcripts with expert labels.
- **Labeling Guidelines**: Co-developed with clinicians.
- **Bias Mitigation**: Balanced sampling, fairness audits.

## Evaluation Metrics
- **Accuracy / F1** by class.
- **Recall on Critical/High** (priority safety requirement).
- **Latency** (real-time classification).
- **Human agreement** with counselor decisions.

## Privacy & Compliance
- PII redaction and encryption at rest/in transit.
- Access control and audit trails.
- Data retention policy aligned with local regulations.

## Next Steps
1. Gather requirements with stakeholders.
2. Define labeling rubric and create pilot dataset.
3. Build baseline classifier and evaluation pipeline.
4. Run limited pilot with human-in-the-loop.
5. Iterate with safety and fairness reviews.
