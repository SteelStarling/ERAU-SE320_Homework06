"""Streamlit front-end for NASA's DONKI API
Author: Taylor Hancock
Date:   04/16/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

import streamlit as st

# Create pages from files
cme_recent_page = st.Page(
    "pages/coronal_mass_ejections.py",
    title="Most Recent CME Data",
    icon=":material/flare:"
)

cme_json_page = st.Page(
    "pages/json_viewer.py",
    title="CME JSON Viewer",
    icon=":material/data_object:"
)

# Compile pages into navigation bar (with section headers)
pg = st.navigation(
    {
        "Coronal Mass Ejections": [cme_recent_page, cme_json_page]
    }
)

# Run streamlit file
pg.run()
