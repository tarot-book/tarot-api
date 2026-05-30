from rest_framework import serializers

from api.models import Deck, Source


class DeckRefSerializer(serializers.ModelSerializer):
    """Small embedded deck shape used by the source detail endpoint."""

    class Meta:
        model = Deck
        fields = ("id", "name", "image", "description")


class SourceListSerializer(serializers.ModelSerializer):
    """Serializer for GET /api/sources.

    Serializers are DRF's boundary between Django model objects and JSON.
    This one intentionally mirrors the old Go SourceListItem contract.
    """

    class Meta:
        model = Source
        fields = ("id", "name")


class SourceDetailSerializer(serializers.ModelSerializer):
    """Serializer for GET /api/sources/<id> with related decks included."""

    decks = DeckRefSerializer(many=True, read_only=True)

    class Meta:
        model = Source
        fields = ("id", "name", "decks")
