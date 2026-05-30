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

Create `.env` in the repository root using the variables shown below, then run:

```bash
docker compose up -d

cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
./load_fixtures.sh
python manage.py runserver
```

Default address:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Environment variables

The local Django app and `docker-compose.yml` read database settings from `.env` in
the repository root.

```env
DB_USER=tarot
DB_PASSWORD=tarot
DB_NAME=tarot
DB_HOST=127.0.0.1
DB_PORT=5432
```

## Database initialization

`docker compose up -d` starts PostgreSQL and keeps its data in the
`postgres-data` Docker volume. It does not load application data by itself.

For a fresh database, run Django migrations first, then load JSON fixtures:

```bash
cd backend
python manage.py migrate
./load_fixtures.sh
```

The fixture loader imports data from `backend/fixtures` in dependency order:
sources, decks, spreads, suits, ranks, cards, images, deck-source links and
meanings.

To refresh fixture files from the current database state:

```bash
cd backend
./dump_fixtures.sh
```

If you need to recreate the database from scratch, remove the Docker volume and
then repeat the migration and fixture-loading steps:

```bash
docker compose down -v
docker compose up -d
cd backend
python manage.py migrate
./load_fixtures.sh
```

## Versioning

We use **Semantic Versioning** for releases.

* Start with `0.x` while the API contract is still moving.
* When endpoints/response formats are considered stable, bump to `1.0.0`.
* Tag releases in Git (`v0.1.0`, `v0.1.1`, ...).

## License

MIT
