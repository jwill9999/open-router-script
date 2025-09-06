# Open Router Script

This project provides a command-line chat client (`chat_cli.py`) for interacting with OpenRouter or similar chat APIs. It is designed for easy integration and automation of chat-based workflows.

## Features
- Simple CLI for sending and receiving chat messages
- Easily configurable for different endpoints
- Supports basic authentication and message formatting

## Usage
1. Clone the repository or copy the script to your local machine.
2. Run the script using Python:
   ```zsh
   python3 chat_cli.py
   ```
3. Follow the prompts to send messages or automate chat interactions.

## Requirements
- Python 3.7+
- Any required dependencies (see script for details)

## Configuration
You can modify the script to point to your desired chat API endpoint and adjust authentication as needed.

## License
MIT License

## Author
letuscode

## Commands and Properties
| Command / Option                | Description                                                                                 | Example Usage                                                      |
|---------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `python3 chat_cli.py "question"`| Run the script with a question as argument                                                   | `python3 chat_cli.py "What is the meaning of life?"`              |
| `echo "question" | python3 chat_cli.py` | Pipe a question from stdin                                                                | `echo "What's new in AI?" | python3 chat_cli.py`                 |
| `-m`, `--model`                 | Specify model ID (overrides $MODEL env variable)                                             | `python3 chat_cli.py -m meta-llama/llama-3.1-8b-instruct "Question"` |
| `--version`                     | Show program version and exit                                                               | `python3 chat_cli.py --version`                                    |
| `--print-alias`                 | Print a suggested zsh alias for the script and exit                                         | `python3 chat_cli.py --print-alias`                                |
| `-h`, `--help`                  | Show help message with all options                                                          | `python3 chat_cli.py -h`                                           |
| `MODEL` (env var)               | Default model to use if --model is not provided                                             | `export MODEL=qwen/qwen3-30b-a3b-thinking-2507`                    |
| `OPENROUTER_API_KEY` (env var)  | Required. Your OpenRouter API key                                                           | `export OPENROUTER_API_KEY=sk-or-...`                              |
