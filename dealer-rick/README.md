# Dealer Rick - Blackjack Discord Bot

## Overview
Dealer Rick is a Discord bot designed to bring the classic game of Blackjack to your server. With features like a coin system, user interactions, and a fun UI for displaying cards, this bot aims to provide an engaging gaming experience for all users.

## Features
- **Traditional Blackjack Rules**: Play with standard rules, including splitting and doubling down.
- **Coin System**: Each user starts with 1000 coins. Users can earn or lose coins based on their gameplay.
- **Bankruptcy Notifications**: If a user goes bankrupt, the bot will notify the server, adding a humorous touch to the experience.
- **Persistent User Data**: Users can return to the game with the same amount of coins they had previously.
- **Card UI**: A visually appealing representation of cards to enhance the gaming experience.

## Project Structure
The project is organized into several directories and files:

- **src/**: Contains the main bot logic and game mechanics.
  - **bot.py**: The entry point for the Discord bot.
  - **commands/**: Contains command logic for the bot.
    - **blackjack.py**: Handles the Blackjack game commands.
    - **economy.py**: Manages the coin system.
  - **game/**: Contains classes and logic related to the game.
    - **card.py**: Defines the Card class.
    - **deck.py**: Manages the deck of cards.
    - **hand.py**: Represents a player's hand.
    - **blackjack_game.py**: Main game logic.
  - **database/**: Manages user data and persistence.
    - **user_manager.py**: Handles user data storage and retrieval.
  - **ui/**: Responsible for rendering the UI elements.
    - **card_renderer.py**: Displays cards in Discord.
  - **utils/**: Contains utility functions and constants.
    - **constants.py**: Defines constants used throughout the project.

- **assets/**: Contains image assets for the playing cards.

- **config/**: Configuration settings for the bot.

- **requirements.txt**: Lists the dependencies required for the project.

- **.env.example**: Template for environment variables.

- **.gitignore**: Specifies files to be ignored by Git.

- **railway.json**: Configuration for deploying the bot on Railway.

## Setup Instructions
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```
3. **Configure Environment Variables**: Copy `.env.example` to `.env` and fill in the required values, such as your Discord bot token.
4. **Run the Bot**: Start the bot by executing:
   ```
   python src/bot.py
   ```

## Usage
Once the bot is running, users can interact with it in Discord by using commands to play Blackjack, check their coin balance, and more. Enjoy the game and may the odds be in your favor!

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.