import random
from src.game.card import Card
from src.utils.constants import SUITS, RANKS


class Deck:
    """This represents a standard deck of 52 playing cards."""

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """Resets the deck to a full 52-card deck and shuffles it."""
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal(self) -> Card:
        """Deals a single card from the deck. If the deck is empty, it resets and shuffles."""
        if len(self.cards) == 0:
            self.reset()
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
