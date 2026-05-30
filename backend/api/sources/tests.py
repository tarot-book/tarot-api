from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Deck, Source


class SourceAPITests(APITestCase):
    def test_list_sources(self):
        first = Source.objects.create(name="First source")
        second = Source.objects.create(name="Second source")

        response = self.client.get("/api/sources")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {"id": first.id, "name": "First source"},
                {"id": second.id, "name": "Second source"},
            ],
        )

    def test_get_source_by_id_with_decks(self):
        source = Source.objects.create(name="Book source")
        deck = Deck.objects.create(
            name="Rider-Waite",
            image="rider-waite.jpg",
            description="Classic deck",
        )
        deck.sources.add(source)

        response = self.client.get(f"/api/sources/{source.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": source.id,
                "name": "Book source",
                "decks": [
                    {
                        "id": deck.id,
                        "name": "Rider-Waite",
                        "image": "rider-waite.jpg",
                        "description": "Classic deck",
                    }
                ],
            },
        )

    def test_get_unknown_source_returns_404(self):
        response = self.client.get("/api/sources/999")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sources_are_read_only_for_now(self):
        response = self.client.post("/api/sources", {"name": "New source"})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
