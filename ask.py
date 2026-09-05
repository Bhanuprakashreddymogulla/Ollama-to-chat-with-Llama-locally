"""
Ask a Single Question - Ollama + Llama
----------------------------------------
A simple script to ask one question to your local Ollama model and get a response.
Unlike chat.py, this doesn't keep conversation history - it's for quick one-off questions.

Requirements:
    - Ollama installed and running (https://ollama.com)
    - A model pulled locally, e.g.: ollama pull llama3.2

Usage:
    python3 ask.py
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:latest"  # change this if you're using a different model


def ask_question(question):
    """Send a single question to Ollama and print the streamed response."""
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": question}],
            "stream": True
        },
        stream=True
    )

    print("Llama: ", end="", flush=True)
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            content = chunk.get("message", {}).get("content", "")
            print(content, end="", flush=True)
    print()


def main():
    print(f"Ask a question to '{MODEL_NAME}' via Ollama.\n")
    question = input("Your question: ").strip()

    if question:
        ask_question(question)
    else:
        print("No question entered.")


if __name__ == "__main__":
    main()
