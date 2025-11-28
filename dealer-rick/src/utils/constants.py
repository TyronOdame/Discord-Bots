# Constants for Dealer Rick Blackjack Bot

# Card suits
SUITS = ["♠️", "♥️", "♦️", "♣️"]

# Card ranks
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Card values
CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}  # Ace can also be 1, handled in game logic

# Blackjack rules
BLACKJACK = 21
DEALER_STAND_VALUE = 17
BLACKJACK_PAYOUT = 1.5

# Starting coins for users
STARTING_COINS = 1000

# Bankruptcy message
BANKRUPTCY_MESSAGE = "Hey everyone, {user_name} just lost everything in blackjack, laugh at this loser one time."

# Game states
GAME_STATE_IDLE = "idle"
GAME_STATE_IN_PROGRESS = "in_progress"
GAME_STATE_FINISHED = "finished"
