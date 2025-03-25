"""Tests for the application module
Author: Taylor Hancock, based on Wolf Paulus's JSON_View file
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

from streamlit.testing.v1 import AppTest

def test_ui_values():
    """Test to ensure the UI displayed in the application is correct"""
    apptest = AppTest.from_file("./app/Coronal_Mass_Ejections.py")
    apptest.run(timeout = 20)

    assert apptest.title[0].value.startswith("Most Recent Coronal Mass Ejection")
    assert apptest.header[0].value.startswith("Last CME:")
    assert not apptest.exception
