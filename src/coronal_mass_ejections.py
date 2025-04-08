"""Streamlit front-end for NASA's Coronal Mass Ejection API
Author: Taylor Hancock
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

import pandas as pd
import streamlit as st
# import altair as alt
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
st.title("Most Recent Coronal Mass Ejection")

updat_btn = st.sidebar.button("Update", type = "primary", on_click = reload_data)

st.header(f"Last CME: {last_updated(cme_data)}")

data_points = ["startTime", "cmeAnalyses.type", "cmeAnalyses.speed", "cmeAnalyses.halfAngle"]
for cme in cme_data:
    cme["cmeAnalyses"] = cme["cmeAnalyses"][0]
cme_normalized = pd.json_normalize(cme_data)

chart_data = pd.DataFrame(cme_normalized, columns = data_points)

last_data = chart_data.iloc[-1]

with st.container(border=True):
    col1, col2, col3= st.columns(3)
    col1.metric("Type", f"{last_data['cmeAnalyses.type']}")
    col2.metric("Speed", f"{last_data['cmeAnalyses.speed']} km/s")
    col3.metric("Half Angle (Width)", f"{last_data['cmeAnalyses.halfAngle']}°")

# removed for future work
# chart = (
#     alt.Chart(chart_data)
#     .mark_circle()
#     .encode(
#         x=alt.X("startTime", title="Day"),
#         y=alt.Y("cmeAnalyses.speed", title="Speed"),
#         # size=alt.Size("cmeAnalyses.type", title="Type"),
#     )
# )
# st.altair_chart(chart, use_container_width=True, theme=None)
