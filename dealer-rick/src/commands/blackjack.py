from discord.ext import commands
import random
from src.game.blackjack_game import BlackjackGame
from src.database.user_manager import UserManager
from src.ui.card_renderer import CardRenderer

class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_manager = UserManager()
        self.card_renderer = CardRenderer()

    @commands.command(name='blackjack')
    async def play_blackjack(self, ctx):
        user_id = ctx.author.id
        user_data = self.user_manager.get_user_data(user_id)

        if user_data['coins'] <= 0:
            await ctx.send(f"You have no coins left! You need to get more coins to play.")
            return

        game = BlackjackGame(user_data['coins'])
        await ctx.send(f"{ctx.author.mention} has started a game of Blackjack!")

        while True:
            await ctx.send("Type 'hit' to take a card, 'stand' to hold, 'double' to double down, or 'split' to split your hand.")
            response = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

            if response.content.lower() == 'hit':
                card = game.hit()
                await ctx.send(f"You drew: {self.card_renderer.render_card(card)}")
            elif response.content.lower() == 'stand':
                break
            elif response.content.lower() == 'double':
                if user_data['coins'] < game.current_bet:
                    await ctx.send("You don't have enough coins to double down!")
                else:
                    game.double_down()
                    await ctx.send("You doubled down!")
            elif response.content.lower() == 'split':
                if not game.can_split():
                    await ctx.send("You cannot split your hand!")
                else:
                    game.split()
                    await ctx.send("You split your hand!")
            else:
                await ctx.send("Invalid command. Please try again.")

        result = game.resolve_game()
        await ctx.send(result)

        if user_data['coins'] <= 0:
            await ctx.send(f"Hey everyone, {ctx.author.name} just lost everything in blackjack, laugh at this loser one time!")
            self.user_manager.handle_bankruptcy(user_id)

def setup(bot):
    bot.add_cog(Blackjack(bot))