class BlackjackGame:
    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer
        self.deck = None
        self.current_bets = {}
        self.game_over = False

    def start_game(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deal_initial_cards()
        self.game_loop()

    def deal_initial_cards(self):
        for player in self.players:
            player.add_card(self.deck.deal_card())
            player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def game_loop(self):
        while not self.game_over:
            for player in self.players:
                self.player_turn(player)
                if self.game_over:
                    break
            if not self.game_over:
                self.dealer_turn()
                self.determine_winners()

    def player_turn(self, player):
        # Logic for player's turn (hit, stand, double down, split)
        pass

    def dealer_turn(self):
        # Logic for dealer's turn
        pass

    def determine_winners(self):
        # Logic to determine winners and handle payouts
        pass

    def reset_game(self):
        self.game_over = True
        self.current_bets.clear()
        for player in self.players:
            player.reset_hand()
        self.dealer.reset_hand()