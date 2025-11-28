# Contents of /dealer-rick/src/bot.py

import discord
from discord.ext import commands
import os

# Load configuration
from config.config import TOKEN, COMMAND_PREFIX

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Load commands
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

# Load command modules
for filename in os.listdir('./src/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Run the bot
bot.run(TOKEN)