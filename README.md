# Ollama-to-chat-with-Llama-locally

A simple Python project for interacting with a Llama model fully offline using [Ollama](https://ollama.com). No external API calls, no internet required once the model is downloaded — everything runs locally on your machine.

## Features

- Chat with a local Llama model directly from the terminal
- Ask quick one-off questions without a full conversation
- Streams responses in real time
- Maintains conversation history within a chat session (context-aware replies)
- Fully offline — no API keys or internet needed after setup

## Tech Stack

- Python
- Ollama (local LLM runtime)
- Llama 3.2 model

## Requirements

- [Ollama](https://ollama.com) installed and running
- A Llama model pulled locally, e.g.:
  ```
  ollama pull llama3.2
  ```
- Python 3.9+

## Setup

1. Clone this repo:
   ```
   git clone https://github.com/Bhanuprakashreddymogulla/Ollama-to-chat-with-Llama-locally.git
   cd Ollama-to-chat-with-Llama-locally
   ```

2. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```

## Usage

### Full Chat (chat.py)

Run a back-and-forth conversation with context maintained across the session:
```
python3 chat.py
```

```
You: Hello, how are you?
Llama: Hello! I'm functioning properly and ready to assist you...
```

Type `exit` or `quit` to end the chat.

### Quick Question (ask.py)

For a single, one-off question with no conversation history:
```
python3 ask.py
```

```
Your question: what is data engineering?
Llama: Data engineering is...
```

## Why This Project

Running LLMs locally (instead of relying on cloud APIs) is useful for privacy, cost control, and offline use cases. This project is a small hands-on exploration of local LLM deployment using Ollama, as a step toward building more advanced GenAI and agentic AI applications.

## License

MIT
