# Template Discord Bot

## Description

This is a Discord bot template that has the particularity of being managed by your API.

### Merge of:

* **Discord**
* **Discord Slash Command**
* **BlackSheep**
* **Django ORM**

## Dependencies

### Required

* **Python 3.10**
* [**Pipenv**](https://github.com/pypa/pipenv)
* **PostgreSQL**

### Recommended

* [**Pyenv**](https://github.com/pyenv/pyenv)

## Installation

### Python dependencies

```bash
pipenv sync --dev
```

***Basic usage of pipenv***

* *Start shell environment:*

```bash
pipenv shell
```

### Database

If you don't have PostgreSQL installed, you can use Docker:

```bash
docker-compose up -d
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

# Django ORM
DB_NAME=<YOUR_DATABASE_NAME>
DB_USER=<YOUR_DATABASE_USER>
DB_PASSWORD=<YOUR_DATABASE_PASSWORD>
DB_HOST=<YOUR_DATABASE_HOST>
DB_PORT=<YOUR_DATABASE_PORT>
```

### Initialize Database

*Reset database and apply migrations.*

```bash
python main.py init_bdd
```

### Local settings

To override the development settings, you can create `local.py` file in the `settings` folder:

```python
from .dev import *  # noqa

# Your code here
```

*To use these settings, you must add this environment variable: `EXEC_PROFILE=local`.*

## Usage

Start server:

```bash
python main.py runserver
```

> With `-r` or `--reload` you can activate the automatic reloading at each modification.
>
> With `-p <PORT>` or `--port <PORT>` you can change port.
>
> With `-l` or `--logs` you can save custom logs in `logs/<date>.txt`.
