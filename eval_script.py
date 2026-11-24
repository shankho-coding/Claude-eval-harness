import anthropic

client = anthropic.Anthropic()
MODEL = "claude-sonnet-5-5"

# Each test has a question and a rubric: what a correct answer must convey.
test_cases = [
    {
        "question": "What is the bullwhip effect in one or two sentences?",
        "rubric": "Must explain that small changes in consumer demand cause progressively larger swings in orders or inventory further up the supply chain.",
    },
    {
        "question": "What does safety stock protect against? Answer briefly.",
        "rubric": "Must say it protects against uncertainty in demand and/or supply lead time, to avoid stockouts.",
    },
    {
        "question": "In supply planning, what is the difference between a master production schedule and MRP? Answer briefly.",
        "rubric": "Must say the MPS plans quantities and timing of finished products, while MRP derives the materials and components needed to meet that schedule.",
    },
]


def ask_claude(question):
    """Get an answer from Claude."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text


def grade_answer(question, answer, rubric):
    """Ask Claude to act as a grader. Returns True if the answer passes."""
    grading_prompt = f"""You are grading an answer to a question.

Question: {question}

Answer to grade: {answer}

Rubric: {rubric}

Does the answer satisfy the rubric? Reply with only one word: PASS or FAIL."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=10,
        messages=[{"role": "user", "content": grading_prompt}],
    )
    verdict = response.content[0].text.strip().upper()
    return verdict.startswith("PASS")


def run_eval():
    passed = 0
    for i, case in enumerate(test_cases, start=1):
        answer = ask_claude(case["question"])
        if grade_answer(case["question"], answer, case["rubric"]):
            passed += 1
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print(f"  Answer was: {answer[:200]}...")
    print(f"\nScore: {passed}/{len(test_cases)}")


if __name__ == "__main__":
    run_eval()