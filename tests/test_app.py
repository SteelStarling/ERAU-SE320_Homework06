"""Tests for the application module
Author: Taylor Hancock, based on Wolf Paulus's JSON_View file
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

from streamlit.testing.v1 import AppTest

def test_cme_recent_values():
    """Test to ensure the UI displayed in the CME page is correct"""
    apptest = AppTest.from_file("../src/pages/coronal_mass_ejections.py")
    apptest.run(timeout = 20)

    assert apptest.title[0].value.startswith("Most Recent Coronal Mass Ejection")
    assert apptest.header[0].value.startswith("Last CME:")
    assert not apptest.exception

def test_cme_json_values():
    """Test to ensure the UI displayed in the application is correct"""
    apptest = AppTest.from_file("../src/pages/json_viewer.py")
    apptest.run(timeout = 20)

    assert apptest.title[0].value.startswith("Coronal Mass Ejections")
    assert apptest.subheader[0].value.startswith("Covers events from")
    assert not apptest.exception
