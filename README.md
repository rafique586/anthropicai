# anthropicai

A small personal repository used to keep Claude/AI-generated code snippets and experiments.

Currently this repo contains a single script, `main.py`, which sends one message to Claude and prints the reply. (An earlier version of this script called the OpenAI API instead, which didn't match the repo's stated purpose — it's since been switched to the Anthropic API.)

## What it does

`main.py` creates an Anthropic client, sends a single hardcoded prompt to `claude-sonnet-5`, and prints the response text. There is no CLI, configuration, or error handling — it's a minimal one-off script.

## Tech stack

- Python 3
- [`anthropic`](https://pypi.org/project/anthropic/) Python SDK

## Setup / run

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python main.py
```

## Project structure

```
main.py             # single script: sends one message to Claude and prints the reply
requirements.txt    # single dependency: anthropic
```

This repo is a scratch space for AI-related code snippets, so structure and contents are expected to evolve over time. Given its current size (a single ~10-line script), a separate architecture document isn't warranted yet.
