import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime
from config import DISCORD_TOKEN, CHECK_INTERVAL_HOURS
from fmp_client import fetch_economic_events, filter_events, format_event_for_discord, get_fomc_events

# Bots setup with intents / permissions on requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ID of channel where bot lives
CHANNEL_ID = None

@bot.event
async def on_ready():

    """ When bot is ready, prints a entrence message + sets the channel ID """
    global CHANNEL_ID
    print(f'{bot.user} has tapped Nacy Pelosi\'s phone notifications ')

    """ start background tasks """
    if not check_for_events.is_running():
        check_for_events.start()

    """ Print avalible channels for debugging """
    print(f"Bot is in {len(bot.guilds)} server(s):")

@tasks.loop(hours=CHECK_INTERVAL_HOURS)
async def check_for_events():

    """ backgound check that run every CHECK_INTERVAL_HOURS hours and post events to the channel """
    try:
        print(f"Finding Nacy Pelosi's phone signal for events @[{datetime.now()}]...")

        """ Fetch and filter events """
        events = fetch_economic_events()
        filtered_events = filter_events(events)

        """ Get FOMC specific events """
        fomc_events = get_fomc_events(filtered_events)
        
        if not fomc_events:
            print(" Pelosi didn't answer her phone, no FOMC events to report.")
            return

        """ Post FOMC events to the channel """
        channel = bot.get_channel(CHANNEL_ID)

        if not channel:
            print(f"Channel with ID {CHANNEL_ID} not found. Set channel ID in bot.py")
            return

        for event in fomc_events[:5]:
            message = format_event_for_discord(event)
            await channel.send(message)
            print(f"Here's what Nacy Got: {event.get('event', 'Unknown Event')} ")

            await asyncio.sleep(1)

    except Exception as e:
        print(f"Error checking for events: {e}")


@bot.command(name='set_channel')
async def set_channel(ctx):

    """ Command to set the channel where bot will post events """
    global CHANNEL_ID
    CHANNEL_ID = ctx.channel.id
    await ctx.send(f"Updates will be posted to: {ctx.channel.mention}")

def run_bot():
    """ Run the bot with the token from the environment variables """
        if not DISCORD_TOKEN:
            raise ValueError("DISCORD_TOKEN is not set in environment variables")

        bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    run_bot()