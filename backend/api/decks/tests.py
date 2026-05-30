from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

from api.enums import ArcanaType
from api.models import Card, CardMinor, Deck, Rank, Source, Suit


@override_settings(CARD_IMAGE_BASE_URL="http://static.example")
class DeckAPITests(APITestCase):
    def test_list_decks(self):
        major_only = Deck.objects.create(
            name="Major only",
            image="major/cover.png",
            description="Major cards only",
        )
        full_deck = Deck.objects.create(
            name="Full deck",
            image="/full/cover.png",
            description="Major and minor cards",
        )
        suit = Suit.objects.create(name="Cups", genitive="Cups", description="")
        rank = Rank.objects.create(name="Ace")
        card = Card.objects.create(deck=full_deck, arcana=ArcanaType.MINOR)
        CardMinor.objects.create(card=card, suit=suit, rank=rank)

        response = self.client.get("/api/decks")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": major_only.id,
                    "name": "Major only",
                    "image": "http://static.example/images/major/cover.png",
                    "thumbnail": "http://static.example/thumbnails/major/cover.png",
                    "description": "Major cards only",
                    "hasMinorCards": False,
                },
                {
                    "id": full_deck.id,
                    "name": "Full deck",
                    "image": "http://static.example/images/full/cover.png",
                    "thumbnail": "http://static.example/thumbnails/full/cover.png",
                    "description": "Major and minor cards",
                    "hasMinorCards": True,
                },
            ],
        )

    def test_get_deck_by_id_with_sources(self):
        source = Source.objects.create(name="Book source")
        deck = Deck.objects.create(
            name="Rider-Waite",
            image="rider/cover.png",
            description="Classic deck",
        )
        deck.sources.add(source)

        response = self.client.get(f"/api/decks/{deck.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": deck.id,
                "name": "Rider-Waite",
                "image": "http://static.example/images/rider/cover.png",
                "thumbnail": "http://static.example/thumbnails/rider/cover.png",
                "description": "Classic deck",
                "hasMinorCards": False,
                "sources": [
                    {
                        "id": source.id,
                        "name": "Book source",
                    }
                ],
            },
        )

    def test_get_unknown_deck_returns_404(self):
        response = self.client.get("/api/decks/999")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_decks_are_read_only_for_now(self):
        response = self.client.post("/api/decks", {"name": "New deck"})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
