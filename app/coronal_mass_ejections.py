"""Streamlit front-end for NASA's Coronal Mass Ejection API
Author: Taylor Hancock
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

import pandas as pd
import streamlit as st
import altair as alt
from data import get_data, reload_data, last_updated

# Configure header info
st.set_page_config(
    page_title = "Coronal Mass Ejections",
    page_icon  = "☀️"
)

# Hide header with CSS
st.markdown(
    """
    <style>
        header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html = True
)

cme_data = get_data()
events = cme_data