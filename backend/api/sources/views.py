from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.models import Source

from .serializers import SourceDetailSerializer, SourceListSerializer


class SourceListView(ListAPIView):
    """Read-only list endpoint for interpretation sources."""

    # DRF evaluates this queryset when handling the request and passes the
    # resulting model objects into SourceListSerializer.
    queryset = Source.objects.order_by("id")
    serializer_class = SourceListSerializer


class SourceDetailView(RetrieveAPIView):
    """Read-only detail endpoint for a single interpretation source."""

    # prefetch_related avoids an extra query per source when the serializer reads
    # the many-to-many `decks` relation.
    queryset = Source.objects.prefetch_related("decks").order_by("id")
    serializer_class = SourceDetailSerializer
