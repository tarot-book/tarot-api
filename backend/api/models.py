from django.db import models

from .enums import ArcanaType, CardPosition


class Deck(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment="a name")
    description = models.TextField(blank=True, null=True, db_comment="desc description")
    image = models.CharField(max_length=255)

    sources = models.ManyToManyField(
        "Source",
        related_name="decks",
        through="DeckSource",
    )

    class Meta:
        managed = True
        db_table = "deck"
        db_table_comment = "Taro deck"

    def __str__(self) -> str:
        return self.name


class Source(models.Model):
    name = models.CharField(unique=True, max_length=255, db_comment="a name")

    class Meta:
        managed = True
        db_table = "source"
        db_table_comment = "Sources of interpretations"

    def __str__(self) -> str:
        return self.name

class DeckSource(models.Model):
    id = models.BigAutoField(primary_key=True)

    deck = models.ForeignKey(
        "Deck",
        models.DO_NOTHING,
        db_column="deck",
        related_name="deck_sources",
    )
    source = models.ForeignKey(
        "Source",
        models.DO_NOTHING,
        db_column="source",
        related_name="source_decks",
    )

    class Meta:
        managed = True
        db_table = "deck_source"
        unique_together = (("deck", "source"),)

    def __str__(self) -> str:
        return f"{self.deck} ↔ {self.source}"

class Spread(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment="spread name")
    major_arcana = models.BooleanField()
    minor_arcana = models.BooleanField()
    upside_down = models.BooleanField()
    num_cards = models.SmallIntegerField(db_comment="number of cards in the spread")
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "spread"
        db_table_comment = "Card spreads"

    def __str__(self) -> str:
        return self.name


class Suit(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment="name as nominative")
    genitive = models.CharField(max_length=100, db_comment="name as genitive")
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "suit"
        db_table_comment = "Minor Arcana suits"

    def __str__(self) -> str:
        return self.name


class Rank(models.Model):
    name = models.CharField(unique=True, max_length=100, db_comment="rank name")

    class Meta:
        managed = True
        db_table = "rank"
        db_table_comment = "Minor Arcana ranks"

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    deck = models.ForeignKey(
        "Deck",
        models.DO_NOTHING,
        db_column="deck",
        related_name="cards",
    )
    arcana = models.CharField(
        max_length=5,
        choices=ArcanaType.choices,
        db_comment="type of Arcana",
    )

    def __str__(self) -> str:
        return f"Card #{self.pk} ({self.arcana})"

    class Meta:
        managed = True
        db_table = "card"


class CardImage(models.Model):
    card = models.OneToOneField(
        Card,
        models.DO_NOTHING,
        db_column="card",
        primary_key=True,
        db_comment="card id",
        related_name="image",
    )
    path = models.CharField(max_length=255, db_comment="relative path to the card image")

    class Meta:
        managed = True
        db_table = "card_image"

    def __str__(self) -> str:
        return self.path


class CardMajor(models.Model):
    card = models.OneToOneField(
        Card,
        models.DO_NOTHING,
        db_column="card",
        primary_key=True,
        db_comment="reference to card id, primary key",
        related_name="major",
    )
    number = models.SmallIntegerField(db_comment="ordinal number in a deck")
    name = models.CharField(max_length=50, db_comment="card name")
    orgname = models.CharField(max_length=50, blank=True, null=True, db_comment="original name")

    class Meta:
        managed = True
        db_table = "card_major"
        db_table_comment = "Major Arcana cards"

    def __str__(self) -> str:
        return f"{self.number}. {self.name}"


class CardMinor(models.Model):
    card = models.OneToOneField(
        Card,
        models.DO_NOTHING,
        db_column="card",
        primary_key=True,
        db_comment="reference to card id, primary key",
        related_name="minor",
    )
    suit = models.ForeignKey(
        "Suit",
        models.DO_NOTHING,
        db_column="suit",
        db_comment="reference to suit",
    )
    rank = models.ForeignKey(
        "Rank",
        models.DO_NOTHING,
        db_column="rank",
        db_comment="reference to rank",
    )

    class Meta:
        managed = True
        db_table = "card_minor"
        db_table_comment = "Minor Arcana cards"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"




class MeaningMajor(models.Model):
    number = models.SmallIntegerField(db_comment="card number")
    position = models.CharField(
        max_length=8,
        choices=CardPosition.choices,
        db_comment="card position",
    )
    source = models.ForeignKey("Source", models.DO_NOTHING, db_column="source", related_name="major_meanings")
    meaning = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Major #{self.number} [{self.position}] ({self.source})"

    class Meta:
        managed = True
        db_table = "meaning_major"
        unique_together = (("number", "position", "source"),)


class MeaningMinor(models.Model):
    suit = models.ForeignKey("Suit", models.DO_NOTHING, db_column="suit", related_name="minor_meanings")
    rank = models.ForeignKey("Rank", models.DO_NOTHING, db_column="rank", related_name="minor_meanings")
    position = models.CharField(
        max_length=8,
        choices=CardPosition.choices,
    )
    source = models.ForeignKey("Source", models.DO_NOTHING, db_column="source", related_name="minor_meanings")
    meaning = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit} [{self.position}] ({self.source})"

    class Meta:
        managed = True
        db_table = "meaning_minor"
        unique_together = (("suit", "rank", "position", "source"),)
