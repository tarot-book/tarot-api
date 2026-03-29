#!/usr/bin/env bash
set -euo pipefail

python manage.py loaddata fixtures/source.json
python manage.py loaddata fixtures/deck.json
python manage.py loaddata fixtures/spread.json
python manage.py loaddata fixtures/suit.json
python manage.py loaddata fixtures/rank.json
python manage.py loaddata fixtures/card.json
python manage.py loaddata fixtures/card_major.json
python manage.py loaddata fixtures/card_minor.json
python manage.py loaddata fixtures/card_image.json
python manage.py loaddata fixtures/deck_source.json
python manage.py loaddata fixtures/meaning_major.json
python manage.py loaddata fixtures/meaning_minor.json
