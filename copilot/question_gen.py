import os
import re
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))


def generate_questions(job_description: str, resume: str, n: int = 6) -> list[str]:
    prompt = (
        f"Job description:\n{job_description}\n\nCandidate resume:\n{resume}\n\n"
        f"Generate {n} realistic interview questions this candidate is likely to be "
        "asked for this specific role, based on the overlap and gaps between the JD "
        "and resume. Mix behavioral and technical questions. Return ONLY a numbered "
        "list, one question per line."
    )
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text")
    questions = [
        re.sub(r"^\d+[\.\)]\s*", "", line).strip()
        for line in text.splitlines()
        if line.strip()
    ]
    return questions[:n]
