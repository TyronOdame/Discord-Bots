import requests
from datetime import datetime, timedelta
from typing import List, Dict
from config import FMP_API_KEY, FILTER_IMPACT, FILTER_COUNTRIES, LOOK_AHEAD_DAYS


BASE_URL = "https://financialmodelingprep.com/api/v3/economic_calendar"

# Grabs the economic events within a specific date range
def fetch_economic_events() -> List[Dict]:
    if not FMP_API_KEY:
        raise ValueError("FMP_API_KEY not set in environment variables")

    # Range calculation
    today = datetime.now().date()
    end_date = today + timedelta(days=LOOK_AHEAD_DAYS)

    params = {
        "apikey": FMP_API_KEY,
        'from': str(today),
        'to': str(end_date)
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    events = response.json()
    return events if isinstance(events, list) else []

# Filters through the event and returns only the specified impact and country
def filter_events(events: List[Dict]) -> List[Dist]:
    filtered_events = []

    for events in events:

        """ country check """
        if event.get('country') not in FILTER_COUNTRIES:
            continue

        """ impact check """
        imapct = event.get('impact', '').lower()
        if FILTER_IMPACT != 'all' and impact != FILTER_IMPACT:
            continue

        """ add to filtered list """
        filtered_events.append(event)

    return sorted(filtered_events, key=lambda x: x.get('date', ''))

# formats the event data into a readable discord message
def format_event_for_discord(event: Dict) -> str:
    """ Formatting for Discord message """

    name = event.get('event', 'Unknown Event')
    date_str = event.get('date', 'N/A')
    impact = event.get('impact', 'N/A').upper()
    forecast = event.get('forecast', 'N/A')
    previous = event.get('previous', 'N/A')

    message = (
        f"@MarketMich • {date_str}\n\n"
        f"**{name}**\n"
        f"⚡️ Impact: {impact}\n"
        f"📈 Forecast: {forecast} | Previous: {previous}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
    )

    return message

# filter through events for FOMC meetings
def get_fomc_events(events: List[Dict]) -> List[Dict]:
    fomc_keywords = ['fomc', 'federal open market', 'rate decision']

    return [
        event for event in events
        if any(keyword in event.get('event', '').lower() for keyword in fomc_keywords)
    ]

        