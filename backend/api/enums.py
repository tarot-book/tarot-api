from django.db import models


class ArcanaType(models.TextChoices):
    MINOR = "minor", "Minor"
    MAJOR = "major", "Major"


class CardPosition(models.TextChoices):
    STRAIGHT = "straight", "Straight"
    REVERTED = "reverted", "Reverted"