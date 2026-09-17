import os
from dotenv import load_dotenv

# API Keys
FMP_API_KEY = os.getenv("FMP_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Bot settings 
CHECK_INTERVAL_HOURS = 3  
FILTER_IMPACT = 'high' 
FILTER_COUNTRIES = ['United States']  # Only USD-related events
LOOK_AHEAD_DAYS = 7 
