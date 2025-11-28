class CardRenderer:
    def __init__(self):
        self.card_suits = ['♠', '♥', '♦', '♣']
        self.card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def render_card(self, suit, rank):
        if suit not in self.card_suits or rank not in self.card_ranks:
            raise ValueError("Invalid suit or rank")
        return f"{rank}{suit}"

    def render_hand(self, hand):
        return ', '.join(self.render_card(card.suit, card.rank) for card in hand)

    def render_deck(self, deck):
        return ', '.join(self.render_card(card.suit, card.rank) for card in deck)