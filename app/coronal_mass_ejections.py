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
st.title("Coronal Mass Ejection History")
st.header("for the last 30 days")

updat_btn = st.sidebar.button("Update", type = "primary", on_click = reload_data)

data_points = ["startTime", "speed", "type"]
cme_normalized = pd.json_normalize(cme_data)
with pd.option_context('display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(cme_normalized)
    
full_data = pd.DataFrame(cme_normalized)

chart_data = pd.DataFrame(full_data, columns = data_points)

chart = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x=alt.X("startTime", sort=None, title="Day"),
        y=alt.Y("speed", title="Speed"),
        size=alt.Size("type", title="Wind Speed (mph)"),
    )
)
st.altair_chart(chart, use_container_width=True, theme=None)
