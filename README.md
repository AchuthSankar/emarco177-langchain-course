# LangChain Course Project

This repository is a starter project for learning and experimenting with LangChain in Python. It includes the basic project structure, environment setup, and a simple entry point that can be extended as the course progresses.

## What we built

The project currently includes:

- A Python application entry point in `main.py`
- Environment variable loading via `python-dotenv`
- LangChain and `langchain-openai` dependencies configured in `pyproject.toml`
- Code quality tooling with `black` and `isort`
- A clean starter layout suitable for adding AI workflows, prompts, chains, and tool integrations

The current app is intentionally minimal and prints a startup message, which makes it easy to build on top of during the course.

### Tools we added and what they do

- `langchain`: the main library for building applications with LLMs, prompts, tools, memory, and chains
- `langchain-openai`: integration for OpenAI models and chat APIs inside LangChain workflows
- `python-dotenv`: loads environment variables from a `.env` file so API keys and config stay out of the codebase
- `black`: auto-formats Python code to keep it consistent and readable
- `isort`: automatically sorts Python imports in a clean, standard order

These packages give us a lightweight but practical foundation for experimenting with AI application development while keeping the project clean and maintainable.

## Design

The project follows a simple, beginner-friendly structure:

- `main.py` acts as the application entry point
- `pyproject.toml` defines the project metadata and required Python packages
- `.env` is used to keep secrets such as API keys outside of source control
- LangChain libraries are imported as the foundation for future prompt and model interactions

This keeps the project easy to understand while remaining flexible enough to evolve into a larger LangChain application.

At a high level, the design is intentionally simple:

- the Python app is the execution layer
- environment variables hold secrets and config
- LangChain handles model and prompt orchestration
- formatting tools keep codebase quality consistent as the app grows

That separation makes it easier to add features without mixing configuration, app logic, and AI integration code together.

## Setup

### Prerequisites

- Python 3.13 or newer
- Git
- A GitHub account
- An OpenAI API key

### 1. Install uv

If you do not already have `uv` installed, install it with:

```bash
pip install uv
```

Or follow the official installation instructions for your platform.

### 2. Create a virtual environment and install dependencies

```bash
uv venv
uv sync
```

This creates the project environment and installs the dependencies defined in `pyproject.toml`.

The dependency list in `pyproject.toml` currently includes:

- `langchain`
- `langchain-openai`
- `python-dotenv`
- `black`
- `isort`

If you want to install a package manually with uv, use:

```bash
uv add langchain langchain-openai python-dotenv
```

### 3. Create a `.env` file

Create a file named `.env` in the project root with your credentials:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

> Do not commit your `.env` file to version control.

### 4. Run the app

Activate the environment and run the app:

```bash
uv run python main.py
```

Expected output:

```text
Hello from emarco177-langchain-course!
```

## Project structure

```text
emarco177-langchain-course/
├── .env
├── .gitignore
├── .venv/
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Notes

This project is set up as a foundation for learning LangChain concepts such as:

- model interaction
- prompt templates
- chains and agents
- tool calling
- memory and retrieval
- application integration patterns

As the course advances, this project can be expanded with more realistic AI workflows and application logic.

## Recommended next steps

- Add a reusable LangChain prompt template
- Connect to OpenAI through LangChain
- Build a basic chat or retrieval workflow
- Add structured configuration for environment variables and model settings
- Add tests and production-ready logging

## GitHub remote

If this repository is meant to be pushed to your own fork or personal repository, update the remote URL before pushing:

```bash
git remote set-url origin https://github.com/<your-github-username>/langchain-course.git
```

Then push your branch:

```bash
git push --set-upstream origin <branch-name>
```
