from django.contrib import admin

from .models import (
    Deck,
    Source,
    Spread,
    Suit,
    Rank,
    Card,
    CardMajor,
    CardMinor,
    CardImage,
    MeaningMajor,
    MeaningMinor,
    DeckSource,
)


class DeckSourceInline(admin.TabularInline):
    model = DeckSource
    extra = 0


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ("name",)
    search_fields = ("name",)
    # filter_horizontal = ("sources",)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Spread)
class SpreadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "num_cards", "major_arcana", "minor_arcana", "upside_down")
    search_fields = ("name",)
    list_filter = ("major_arcana", "minor_arcana", "upside_down")


@admin.register(Suit)
class SuitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "genitive")
    search_fields = ("name", "genitive")


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "deck", "arcana")
    list_filter = ("arcana", "deck")
    search_fields = ("id",)


@admin.register(CardMajor)
class CardMajorAdmin(admin.ModelAdmin):
    list_display = ("card", "number", "name", "orgname")
    search_fields = ("name", "orgname")
    list_filter = ("card__deck",)


@admin.register(CardMinor)
class CardMinorAdmin(admin.ModelAdmin):
    list_display = ("card", "rank", "suit")
    list_filter = ("suit", "rank", "card__deck")


@admin.register(CardImage)
class CardImageAdmin(admin.ModelAdmin):
    list_display = ("card", "path")
    search_fields = ("path",)


@admin.register(MeaningMajor)
class MeaningMajorAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "position", "source")
    list_filter = ("position", "source")
    search_fields = ("meaning",)


@admin.register(MeaningMinor)
class MeaningMinorAdmin(admin.ModelAdmin):
    list_display = ("id", "rank", "suit", "position", "source")
    list_filter = ("suit", "rank", "position", "source")
    search_fields = ("meaning",)


@admin.register(DeckSource)
class DeckSourceAdmin(admin.ModelAdmin):
    list_display = ("id", "deck", "source")
    list_filter = ("deck", "source")