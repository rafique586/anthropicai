# anthropicai

A small personal repository used to keep Claude/AI-generated code snippets and experiments.

Currently this repo contains a single script, `main.py`, which sends one chat completion request. Note that despite the repo's name (and description "repository to keep all Claude generated code"), the current script calls the **OpenAI** API (`from openai import OpenAI`, model `gpt-4o-mini`) rather than the Anthropic API — this looks like an early/experimental snippet rather than a finished project.

## What it does

`main.py` creates an OpenAI client, sends a single hardcoded prompt to `gpt-4o-mini`, and prints the response text. There is no CLI, configuration, or error handling — it's a minimal one-off script.

## Tech stack

- Python 3
- [`openai`](https://pypi.org/project/openai/) Python SDK

## Setup / run

```bash
pip install openai
export OPENAI_API_KEY=sk-...
python main.py
```

## Project structure

```
main.py   # single script: sends one chat completion request and prints the reply
```

This repo is a scratch space for AI-related code snippets, so structure and contents are expected to evolve over time. Given its current size (a single ~10-line script), a separate architecture document isn't warranted yet.
