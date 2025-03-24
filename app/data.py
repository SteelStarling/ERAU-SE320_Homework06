"""Systems to get data on Coronal Mass Ejections
Author: Taylor Hancock, code modified from Wolf Paulus
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

from json import dump, load
from datetime import datetime
from dateutil import tz
from requests import get
import streamlit as st

API_URL = "https://api.nasa.gov/DONKI/CME?api_key=DEMO_KEY"
DATA_FILE = "./app/data/cmes.json"

TIMEOUT = 3

@st.cache_data(show_spinner="Fetching data...", ttl=60*10)
def get_data(api_url: str = API_URL, data_file: str = DATA_FILE) -> dict:
    """Fetches data from a file or the API"""
    try:
        # get the past 30 days of CME info
        cme_history = get(url = api_url, timeout = TIMEOUT).json()

        # if fetch worked
        if cme_history:
            # backup to file
            with open(data_file, "w", encodings = "utf-8") as file:
                dump(cme_history, file)
            return cme_history

        # if fetch fails, read from file instead
        with open(data_file, "r", encoding = "utf-8") as file:
            cme_history = load(file)
        st.warning("Using cached forecast data", icon = "⚠️")
        return cme_history

    except OSError as e:
        # IO system error
        st.error(str(e), icon = "‼️")

    except TypeError as e:
        # JSON decoder error
        st.error(str(e), icon = "‼️")

    # otherwise return empty dictionary
    return {}


def reload_data() -> None:
    """Clear cache (next call will have to pull data from the web service)"""
    get_data.clear()


def last_updated(forecast: dict) -> str:
    """Returns string for the timestamp of the last update"""
    date_time = datetime.fromisoformat()
    date_time = date_time.replace(tzinfo=tz.gettz('UTC')).astimezone()
    return date_time.strftime('%A, %B %-d, %Y %-I:%M:%S %p %Z')


# return values if run alone
if __name__ == "__main__":
    print("Testing 123")
    cme_history = get(API_URL, timeout = TIMEOUT).json()