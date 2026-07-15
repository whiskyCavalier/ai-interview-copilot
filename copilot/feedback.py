import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))


def give_feedback(question: str, answer: str) -> str:
    prompt = (
        f"Interview question: {question}\n\nCandidate's typed answer:\n{answer}\n\n"
        "Give brief, structured feedback with three labeled sections:\n"
        "Strong: (what worked)\n"
        "Missing: (what's absent that a strong answer would include)\n"
        "Tighten: (one specific edit to make the answer sharper)\n"
        "Keep the whole response under 100 words."
    )
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")
