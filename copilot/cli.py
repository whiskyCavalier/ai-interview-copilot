import argparse
from .question_gen import generate_questions
from .feedback import give_feedback


def main():
    parser = argparse.ArgumentParser(description="Mock interview practice tool")
    parser.add_argument("--jd", required=True, help="Path to job description text file")
    parser.add_argument("--resume", required=True, help="Path to resume text file")
    parser.add_argument("-n", type=int, default=6, help="Number of questions to generate")
    args = parser.parse_args()

    with open(args.jd) as f:
        jd_text = f.read()
    with open(args.resume) as f:
        resume_text = f.read()

    questions = generate_questions(jd_text, resume_text, n=args.n)

    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question}")
        answer = input("Your answer: ")
        feedback = give_feedback(question, answer)
        print(f"\nFeedback:\n{feedback}")


if __name__ == "__main__":
    main()
