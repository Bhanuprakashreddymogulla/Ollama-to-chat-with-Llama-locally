"""
Local AI Chatbot using Ollama + Llama
---------------------------------------
Runs fully offline. Talks to a locally running Ollama model via its API.

Requirements:
    - Ollama installed and running (https://ollama.com)
    - A model pulled locally, e.g.: ollama pull llama3

Usage:
    python chat.py
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:latest"  # change this if you're using a different model


def chat_with_ollama(messages):
    """Send the full conversation history to Ollama and stream the response."""
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": True
        },
        stream=True
    )

    full_reply = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            content = chunk.get("message", {}).get("content", "")
            print(content, end="", flush=True)
            full_reply += content

    print()  # newline after the full reply
    return full_reply


def main():
    print(f"Local chatbot running on '{MODEL_NAME}' via Ollama.")
    print("Type 'exit' or 'quit' to end the chat.\n")

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended. Goodbye!")
            break

        if not user_input:
            continue

        conversation_history.append({"role": "user", "content": user_input})

        print("Llama: ", end="", flush=True)
        reply = chat_with_ollama(conversation_history)

        conversation_history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
