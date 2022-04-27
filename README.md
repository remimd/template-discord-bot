# Template Discord Bot

## Description

This is a Discord bot template that has the particularity of being managed by your API.

## Dependencies

### Required

* **Python 3.10**
* [**Pipenv**](https://github.com/pypa/pipenv)

### Recommended

* [**Pyenv**](https://github.com/pyenv/pyenv)

## Installation

### Python dependencies

```bash
pipenv sync --dev
```

## Configuration

### .env

Create `.env` file at the root of the project:

```dotenv
# Discord Bot
TOKEN=<YOUR_DISCORD_BOT_TOKEN>

# API
APP_NAME=<YOUR_APP_NAME>
APP_VERSION=<YOUR_APP_VERSION>

API_KEY=<YOUR_CUSTOM_API_KEY>  # Optional
```

### Local settings

To override the development settings, you can create `local.py` file in the `settings` folder:

```python
from .dev import *  # noqa

# Your code here
```

*To use these settings, you must add this environment variable: `EXEC_PROFILE=local`*

## Usage

Start server:

```bash
uvicorn main:app
```
