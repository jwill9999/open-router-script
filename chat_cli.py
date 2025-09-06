#!/usr/bin/env python3
"""
chat_cli.py — Stream a chat completion via OpenRouter from the terminal.

Environment variables:
    OPENROUTER_API_KEY  Required. Your OpenRouter API key.
    MODEL               Optional. Default model to use if --model is not provided.

Examples:
    python3 chat_cli.py "What is the meaning of life?"
    echo "What's new in AI this week?" | python3 chat_cli.py
    python3 chat_cli.py --model qwen/qwen3-30b-a3b-thinking-2507 "Summarize this"

Tip: show all options with -h / --help
    python3 chat_cli.py -h

Setup (zsh): set your OpenRouter API key for the current shell
    export OPENROUTER_API_KEY=sk-or-...
Persist for new terminals (zsh)
    echo 'export OPENROUTER_API_KEY=sk-or-...' >> ~/.zshrc
    source ~/.zshrc

Quick alias (zsh): add this to your ~/.zshrc so you can run `ask` from anywhere
    alias ask='python3 /path/to/the/file/chat_cli.py'
    source ~/.zshrc
Then use:
    ask "Your question"
    ask -m meta-llama/llama-3.1-8b-instruct "Try a different model"
    echo "What's new in AI?" | ask -m qwen/qwen3-30b-a3b-thinking-2507
"""

import os
import sys
import argparse
from openai import OpenAI

__version__ = "0.1.0"

# Simple terminal CLI for OpenRouter streaming chat
# Usage examples:
#   python3 chat_cli.py "What is the meaning of life?"
#   echo "What's new in AI?" | python3 chat_cli.py
#   python3 chat_cli.py   # then type your question when prompted


def get_question_and_model():
    parser = argparse.ArgumentParser(
        description=(
            "Stream a chat completion from OpenRouter.\n\n"
            "Reads the question from an argument, stdin, or an interactive prompt.\n"
            "Prints streamed tokens to stdout; model info goes to stderr."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 chat_cli.py \"What is the meaning of life?\"\n"
            "  echo \"What's new in AI this week?\" | python3 chat_cli.py\n"
            "  MODEL=qwen/qwen3-30b-a3b-thinking-2507 python3 chat_cli.py \"Question\"\n"
            "  python3 chat_cli.py --model meta-llama/llama-3.1-8b-instruct \"Question\"\n\n"
            "Alias (zsh):\n  alias ask='python3 /path/to/the/file/chat_cli.py'\n  source ~/.zshrc\n  ask \"Question\"\n  ask -m meta-llama/llama-3.1-8b-instruct \"Try a different model\"\n  echo \"What's new in AI?\" | ask -m qwen/qwen3-30b-a3b-thinking-2507\n\n"
            "Env:\n  OPENROUTER_API_KEY (required), MODEL (optional default)\n\n"
            "Setup (zsh):\n  export OPENROUTER_API_KEY=sk-or-...\n  # Persist for future terminals\n  echo 'export OPENROUTER_API_KEY=sk-or-...' >> ~/.zshrc\n  source ~/.zshrc\n"
        ),
    )
    parser.add_argument(
        "question",
        nargs="?",
        help="Your question to ask the model (falls back to stdin or interactive prompt)",
    )
    parser.add_argument(
        "-m",
        "--model",
        default=os.getenv("MODEL", "qwen/qwen3-30b-a3b-thinking-2507"),
        help=(
            "Model ID to use. Defaults to $MODEL if set, otherwise "
            "qwen/qwen3-30b-a3b-thinking-2507"
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show program's version number and exit",
    )
    parser.add_argument(
        "--print-alias",
        action="store_true",
        help="Print a suggested zsh alias for this script and exit",
    )

    args = parser.parse_args()

    if getattr(args, "print_alias", False):
        script_path = os.path.abspath(__file__)
        print(f"alias ask='python3 {script_path}'")
        sys.exit(0)

    question = args.question
    if not question and not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    if not question:
        try:
            question = input("Question: ").strip()
        except EOFError:
            question = ""
    if not question:
        print(
            "No question provided. Pass as an argument, pipe via stdin, or type when prompted.",
            file=sys.stderr,
        )
        sys.exit(1)
    return question, args.model


def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("OPENROUTER_API_KEY is not set. Export it before running.")
        print("Example: export OPENROUTER_API_KEY=sk-or-...")
        sys.exit(1)

    question, model = get_question_and_model()

    # Report requested model to stderr (keeps stdout clean for the answer)
    print(f"Requesting model: {model}", file=sys.stderr)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            stream=True,
        )

        served_model_printed = False
        for chunk in stream:
            # Print the server-declared model once if available
            if not served_model_printed:
                served = getattr(chunk, "model", None)
                if served:
                    print(f"Serving model: {served}", file=sys.stderr)
                    served_model_printed = True

            # Each chunk has choices[0].delta for incremental content
            delta = chunk.choices[0].delta
            if delta and getattr(delta, "content", None):
                print(delta.content, end="", flush=True)
        print()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
