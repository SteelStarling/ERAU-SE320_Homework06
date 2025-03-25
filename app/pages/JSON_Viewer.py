"""Streamlit front-end for NASA's Coronal Mass Ejection API
Author: Taylor Hancock, based on Wolf Paulus's JSON_View file
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

import streamlit as st
from data import CME_FILE, first_event, get_data, last_updated

cme_data = get_data()

st.title("Coronal Mass Ejections")
st.subheader(f"Covers events from {first_event(cme_data)} to {last_updated(cme_data)}")
st.json(cme_data, expanded=True)
with open(CME_FILE, encoding="utf-8") as file:
    st.sidebar.download_button(
        "Download JSON", file, file_name="cmes.json",
        mime="application/json", type="primary"
    )
