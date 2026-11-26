"""
 hello_llm.py — Your first OpenAI API call.
 Run it from the repo root: 
    python src/hello_llm.py "What is RAG in one sentence?"
"""

import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

print("OK: client constructed")

def ask_anotherway(question: str) -> str:
    """ send one question to the LLM and return the answer text. """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "you are a AI teacher."},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

def ask(question: str) -> str:
    """ send one question to the LLM and return the answer text. """
    resp = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are concise.",
        input=question,
        temperature=0.3
    )

    return resp.output_text


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]).strip() or "Say hello in one sentence."
    print(ask_anotherway(question))