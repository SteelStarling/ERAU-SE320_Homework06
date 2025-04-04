"""Systems to get data on Coronal Mass Ejections
Author: Taylor Hancock, code modified from Wolf Paulus
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

from json import dump, load
import os

from datetime import datetime
from dateutil import tz
from dotenv import load_dotenv
from requests import get
import streamlit as st

# load environment
load_dotenv()


API_CME_URL     = "https://api.nasa.gov/DONKI/CME"
# API_EPIC_URL    = "https://api.nasa.gov/EPIC/api/natural"
# API_PICTURE_URL = "https://api.nasa.gov/EPIC/archive/natural/"

CME_FILE        = "./app/data/cmes.json"
# EPIC_FILE       = "./app/data/epic.json"
# EPIC_IMAGES     = "./app/data/"

TIMEOUT = 10


@st.cache_data
def get_api_key() -> str | None:
    """Fetches an API key from environment"""

    # read in the API key
    api_key = os.environ.get("API_KEY", None)

    # if no API key is provided, throw error and return None
    if api_key is None:
        st.error("No API key provided", icon = "‼️")

    return api_key


@st.cache_data(show_spinner="Fetching data...", ttl=60*10)
def get_data(*, api_url: str = API_CME_URL, api_addons: str = "", data_file: str = CME_FILE) -> dict:
    """Fetches data from a file or the API"""

    api_key = get_api_key()

    # Gets the CME history
    try:
        # get the past 30 days of CME info
        cme_history = get(url = f"{api_url}?{api_addons}api_key={api_key}", timeout = TIMEOUT).json()

        # if fetch worked
        if cme_history:
            # backup to file
            with open(data_file, "w", encoding = "utf-8") as file:
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


def time_to_string(date_time: str) -> str:
    """Converts an ISO date string to a pretty string"""
    date_time = datetime.fromisoformat(date_time)
    date_time = date_time.replace(tzinfo=tz.gettz('UTC')).astimezone(tz.gettz("MST"))
    return date_time.strftime('%A, %B %d, %Y %I:%M:%S %p %Z')


def first_event(cmes: dict) -> str:
    """Returns string for the timestamp of the first logged event"""
    # first be sure cmes exist
    if cmes:
        return time_to_string(cmes[0]["startTime"])
    return "NULL"


def last_updated(cmes: dict) -> str:
    """Returns string for the timestamp of the last update"""
    # first be sure cmes exist
    if cmes:
        return time_to_string(cmes[-1]["startTime"])
    return "NULL"
