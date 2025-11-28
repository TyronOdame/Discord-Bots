class UserManager:
    def __init__(self, db_file='user_data.json'):
        self.db_file = db_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.users, file)

    def get_user(self, user_id):
        return self.users.get(user_id, {'coins': 1000})

    def add_coins(self, user_id, amount):
        user = self.get_user(user_id)
        user['coins'] += amount
        self.users[user_id] = user
        self.save_users()

    def subtract_coins(self, user_id, amount):
        user = self.get_user(user_id)
        user['coins'] -= amount
        if user['coins'] < 0:
            user['coins'] = 0
            self.bankrupt(user_id)
        self.users[user_id] = user
        self.save_users()

    def bankrupt(self, user_id):
        # Logic to handle bankruptcy, such as notifying the server
        pass

    def get_balance(self, user_id):
        return self.get_user(user_id)['coins']