#!/usr/bin/env bash
set -euo pipefail

mkdir -p fixtures

python manage.py dumpdata api.Source --indent 2 > fixtures/source.json
python manage.py dumpdata api.Deck --indent 2 > fixtures/deck.json
python manage.py dumpdata api.DeckSource --indent 2 > fixtures/deck_source.json
python manage.py dumpdata api.Spread --indent 2 > fixtures/spread.json
python manage.py dumpdata api.Suit --indent 2 > fixtures/suit.json
python manage.py dumpdata api.Rank --indent 2 > fixtures/rank.json
python manage.py dumpdata api.Card --indent 2 > fixtures/card.json
python manage.py dumpdata api.CardMajor --indent 2 > fixtures/card_major.json
python manage.py dumpdata api.CardMinor --indent 2 > fixtures/card_minor.json
python manage.py dumpdata api.CardImage --indent 2 > fixtures/card_image.json
python manage.py dumpdata api.MeaningMajor --indent 2 > fixtures/meaning_major.json
python manage.py dumpdata api.MeaningMinor --indent 2 > fixtures/meaning_minor.json