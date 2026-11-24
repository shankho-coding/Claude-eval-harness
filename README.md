# Claude Evaluation Harness (Supply Chain)

A small Python script that tests how well Claude answers supply chain planning questions and grades the answers automatically.

## What it does

1. Asks Claude a set of supply chain questions through the Claude API.
2. Sends each answer back to Claude, acting as a grader, along with a written rubric describing what a correct answer must say.
3. Prints PASS or FAIL for each question and a final score.

This approach is often called "LLM-as-judge".

## Why I built it

I work in supply chain consulting and wanted hands-on experience with how LLM outputs get evaluated. Testing whether a model is reliable on a specific use case is a core part of deploying AI in enterprise settings, so I started with questions from my own domain.

## How to run it

1. Install Python 3 and the SDK: `pip install anthropic`
2. Get an API key from the Anthropic Console and set it as an environment variable named `ANTHROPIC_API_KEY`. The key is never stored in the code.
3. Run: `python eval_script.py`

## What I learned

- **Keyword grading is brittle.** My first version checked answers for exact keywords. Claude gave a correct answer in different words and was marked wrong (2/3). Writing rubrics and letting a model judge meaning fixed this (3/3).
- **The test design matters as much as the model.** A score only means something if the questions are hard enough and the rubrics are strict enough.
- **Graders can be wrong too.** Any LLM judge should be spot-checked by a human.

## Limitations and next steps

- Only 3 test cases so far, all fairly easy. Next I plan to add harder questions from supply planning work, including questions with a subtly wrong premise.
- I haven't yet validated the grader against human judgments.
- Planned: compare different system prompts and models on the same test set.
