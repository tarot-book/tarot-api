from django.conf import settings
from rest_framework import serializers

from api.models import Deck, Source
from api.utils import join_url


def build_image_url(path: str, thumbnail: bool = False) -> str | None:
    """Build image URLs the same way the old Go API did.

    Deck.image stores a relative file path in the database. API responses expose
    a public URL based on CARD_IMAGE_BASE_URL, with covers under /images or
    /thumbnails. In dev this can point to Django static files; in production it
    can point to CDN, Nginx or another static asset service.
    """

    base_url = getattr(settings, "CARD_IMAGE_BASE_URL", "")
    if not base_url:
        return None

    folder = "thumbnails" if thumbnail else "images"
    return join_url(base_url, folder, path)


class SourceRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ("id", "name")


class DeckListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    hasMinorCards = serializers.BooleanField(source="has_minor_cards")

    class Meta:
        model = Deck
        fields = ("id", "name", "image", "thumbnail", "description", "hasMinorCards")

    def get_image(self, obj):
        return build_image_url(obj.image)

    def get_thumbnail(self, obj):
        return build_image_url(obj.image, thumbnail=True)


class DeckDetailSerializer(DeckListSerializer):
    sources = SourceRefSerializer(many=True, read_only=True)

    class Meta(DeckListSerializer.Meta):
        fields = DeckListSerializer.Meta.fields + ("sources",)
