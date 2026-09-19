# LangChain Course Project

This repository is a starter project for learning and experimenting with LangChain in Python. It includes the basic project structure, environment setup, and a simple entry point that can be extended as the course progresses.

## What we built

The project currently includes:

- A Python application entry point in `main.py`
- Environment variable loading via Python Dotenv
- LangChain and LangChain OpenAI dependencies configured in `pyproject.toml`
- A clean starter layout suitable for adding AI workflows, prompts, chains, and tool integrations

The current app is intentionally minimal and prints a startup message, which makes it easy to build on top of during the course.

## Design

The project follows a simple, beginner-friendly structure:

- `main.py` acts as the application entry point
- `pyproject.toml` defines the project metadata and required Python packages
- `.env` is used to keep secrets such as API keys outside of source control
- LangChain libraries are imported as the foundation for future prompt and model interactions

This keeps the project easy to understand while remaining flexible enough to evolve into a larger LangChain application.

## Setup

### Prerequisites

- Python 3.13 or newer
- Git
- A GitHub account
- An OpenAI API key

### 1. Create and activate a virtual environment

Using `venv`:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -U pip
pip install -e .
```

You can also install the project dependencies directly with:

```bash
pip install langchain langchain-openai python-dotenv
```

### 3. Create a `.env` file

Create a file named `.env` in the project root with your credentials:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

> Do not commit your `.env` file to version control.

### 4. Run the app

```bash
python main.py
```

Expected output:

```text
Hello from emarco177-langchain-course!
```

## Project structure

```text
emarco177-langchain-course/
├── .env.example
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
└── .venv/
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
