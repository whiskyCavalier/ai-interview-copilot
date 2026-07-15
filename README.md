# ai-interview-copilot

A **mock-interview practice tool**: paste a job description and your resume, get a
tailored set of likely interview questions, answer them, and get structured written
feedback on content, clarity, and structure — before your real interview, not during it.

> **Scope note:** this is a prep/practice tool used *before* an interview, not a
> live-assist tool used *during* one. Using AI to generate real-time answers while
> actually interviewing with an employer is dishonest and most employers explicitly
> prohibit it. This repo intentionally has no "listen to the live call and feed me
> answers" feature, and shouldn't be extended to add one.

## What it does
1. Takes a job description + your resume (plain text)
2. Generates 5-8 realistic interview questions tailored to that specific role
3. You answer each one (typed, offline, at your own pace)
4. Gets feedback per answer: what's strong, what's missing, how to tighten it

## Project structure
```
ai-interview-copilot/
├── copilot/
│   ├── __init__.py
│   ├── cli.py             # entrypoint: python -m copilot.cli
│   ├── question_gen.py     # generates tailored questions from JD + resume
│   └── feedback.py          # scores/critiques a typed answer
├── tests/
│   └── test_question_gen.py
├── requirements.txt
└── README.md
```

## Setup
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
```

## Run
```bash
python -m copilot.cli --jd jd.txt --resume resume.txt
```

## Example output
```
Q1: Walk me through a time you had to make a platform-wide change with limited
    downtime tolerance. What was your approach?

Your answer: [you type here]

Feedback:
  Strong: clear before/after metrics, good structure (situation -> action -> result)
  Missing: no mention of how you communicated risk to stakeholders beforehand
  Tighten: the middle section repeats the same point twice — cut one instance
```

## License
MIT
