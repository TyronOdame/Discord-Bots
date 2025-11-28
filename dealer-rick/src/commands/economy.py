# Contents of /dealer-rick/src/commands/economy.py

class EconomyManager:
    def __init__(self):
        self.user_balances = {}
    
    def add_coins(self, user_id, amount):
        if user_id in self.user_balances:
            self.user_balances[user_id] += amount
        else:
            self.user_balances[user_id] = amount

    def subtract_coins(self, user_id, amount):
        if user_id in self.user_balances:
            self.user_balances[user_id] -= amount
            if self.user_balances[user_id] < 0:
                self.user_balances[user_id] = 0
                self.handle_bankruptcy(user_id)
        else:
            self.user_balances[user_id] = 0

    def check_balance(self, user_id):
        return self.user_balances.get(user_id, 0)

    def handle_bankruptcy(self, user_id):
        # This function should notify the server about the user's bankruptcy
        # For example, sending a message to the Discord channel
        user_name = self.get_user_name(user_id)  # Placeholder for user name retrieval
        message = f"Hey everyone, {user_name} just lost everything in blackjack, laugh at this loser one time"
        self.notify_server(message)

    def get_user_name(self, user_id):
        # Placeholder for a method to get the user's name from their ID
        return f"User_{user_id}"

    def notify_server(self, message):
        # Placeholder for a method to send a message to the Discord server
        print(message)  # Replace with actual Discord message sending logic

# Example usage
if __name__ == "__main__":
    economy_manager = EconomyManager()
    economy_manager.add_coins(12345, 500)
    print(economy_manager.check_balance(12345))  # Should print 500
    economy_manager.subtract_coins(12345, 600)  # Should trigger bankruptcy
    print(economy_manager.check_balance(12345))  # Should print 0