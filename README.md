# Template Discord Bot

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
TOKEN=<YOUR_DISCORD_BOT_TOKEN>
```

### Local settings

To override the development settings, you can create `local.py` file in the `settings` folder:

```python
from .dev import *  # noqa

# Your code here
```

*To use these settings, you must add this environment variable: `EXEC_PROFILE=local`*

## Usage

```bash
python main.py
```

> With `-l` or `--logs` you can save logs in `logs/<date>.txt`
