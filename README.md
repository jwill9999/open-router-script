# Open Router Script
This project provides a command-line chat client (`chat_cli.py`) for interacting with OpenRouter or similar chat APIs. Under the hood, it uses the OpenAI Python library to connect to OpenRouter, enabling easy integration and automation of chat-based workflows.



## Features
- Simple CLI for sending and receiving chat messages in the command line.
- Easily configurable for different models using the `-m` or `--model` command-line options.
- Supports API key authentication and basic message formatting (plain text, and limited markdown such as bold and italics).

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

## Getting Started

1. **Install Python**  
   Download and install Python 3.7 or newer from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Recommended)**  
   Open your terminal and run:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   If your script uses a `requirements.txt` file, install dependencies with:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
You can modify the script to point to your desired chat API endpoint and adjust authentication as needed.

## Basic Commands

Before running any commands, **change your directory** to where the script is located. For example, if you saved the script in a folder called `open_router_script`, use:
```sh
cd /path/to/open_router_script
```
Replace `/path/to/open_router_script` with the actual path where you stored the script.

After setting up your environment, you can run the script using the following commands:

### 1. Run with a Question
```sh
python3 chat_cli.py "Your question here"
```
By default, the script uses the model specified in the `MODEL` environment variable (if set). If not set, it uses the script's internal default.

### 2. Specify an API Key
Set your OpenRouter API key before running the script:
```sh
export OPENROUTER_API_KEY=sk-or-your-api-key
```
This is required for authentication.

### 3. Specify a Model
Override the default model by using the `-m` or `--model` option:
```sh
python3 chat_cli.py -m meta-llama/llama-3.1-8b-instruct "Your question here"
```

### 4. Get Help
Show all available options and usage:
```sh
python3 chat_cli.py -h
```

### 5. Check Version
Display the script version:
```sh
python3 chat_cli.py --version
```
## Further reading
 * Retrieves the API key from the environment variables.
 * Beginner: If you're new to handling API keys, consider the following:
 * - You can create an alias in your shell profile (e.g., `.bashrc`, `.zshrc`) to quickly set or retrieve your API key.
 * - Explore secure storage solutions such as password managers, encrypted files, or secret management services (e.g., HashiCorp Vault, AWS Secrets Manager).
 * - Avoid hardcoding API keys in your source code or sharing them publicly.
 * - For more information, see:
 *   - [How to manage API keys securely](https://www.freecodecamp.org/news/how-to-securely-store-api-keys-4d9e7f1c2f5e/)
 *   - [Environment variables best practices](https://12factor.net/config)
 *   - [GitHub: Keeping secrets safe](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-and-storing-encrypted-secrets)
 
## License
MIT License

## Author
letuscode

