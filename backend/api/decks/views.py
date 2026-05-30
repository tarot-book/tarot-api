from django.db.models import Exists, OuterRef
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.models import CardMinor, Deck

from .serializers import DeckDetailSerializer, DeckListSerializer


def decks_with_stats():
    """Return decks with computed fields expected by the old API contract."""

    minor_cards = CardMinor.objects.filter(card__deck=OuterRef("pk"))

    # annotate adds a computed attribute to each Deck instance. Serializers can
    # read it like a regular field via source="has_minor_cards".
    return Deck.objects.annotate(has_minor_cards=Exists(minor_cards)).order_by("id")


class DeckListView(ListAPIView):
    """Read-only list endpoint for tarot decks."""

    queryset = decks_with_stats()
    serializer_class = DeckListSerializer


class DeckDetailView(RetrieveAPIView):
    """Read-only detail endpoint for a tarot deck with related sources."""

    queryset = decks_with_stats().prefetch_related("sources")
    serializer_class = DeckDetailSerializer
