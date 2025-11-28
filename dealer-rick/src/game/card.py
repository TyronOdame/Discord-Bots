from src.utils.constants import CARD_VALUES


class Card:
    """This represents a single playing card with a rank and suit."""

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = CARD_VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def is_ace(self) -> bool:
        return self.rank == "A"
