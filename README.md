# Tarot API

Backend for Tarot Book / Tarot Mini App.

Django-based REST API providing access to Tarot data: decks, cards, spreads, sources and meanings.

## Stack

* **Python** 3.14 (latest stable) ([python.org](https://www.python.org/downloads/?utm_source=chatgpt.com))
* **Django** 5.2 LTS ([djangoproject.com](https://www.djangoproject.com/download/?utm_source=chatgpt.com))
* **Django REST Framework**
* **PostgreSQL**
* **Docker Compose** (local dev)

## Quick start (local)

```bash
docker compose up -d
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Default address:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Environment variables

```env
DATABASE_URL=postgres://tarot:tarot@127.0.0.1:5432/tarot
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Versioning

We use **Semantic Versioning** for releases.

* Start with `0.x` while the API contract is still moving.
* When endpoints/response formats are considered stable, bump to `1.0.0`.
* Tag releases in Git (`v0.1.0`, `v0.1.1`, ...).

## License

MIT
