"""Tests for the data module
Author: Taylor Hancock, based on Wolf Paulus's JSON_View file
Date:   03/24/2025
Class:  SE320 - Software Construction
Assignment: Application UI
"""

from os.path import exists, join
from os import remove

from data import get_data, get_api_key


def test_data_acquisition():
    """Acquire data and verify it makes sense"""
    
    # verify api key exists
    key = get_api_key()
    assert key is not None, "No API key provided"

    path_to_data_file = join("app", "data", "cmes.json")
    if exists(path_to_data_file):
        remove(path_to_data_file)

    # if this fails, something weird is going on
    assert not exists(path_to_data_file), \
        "Error occurred during removal of data file (this is OS side likely...)"
    cme_data = get_data(api_addons = "startDate=2017-01-03&endDate=2017-01-03&")
    assert exists(path_to_data_file), "Data file not created when data is collected"

    example_cme = cme_data[0]

    assert example_cme["activityID"] == "2017-01-03T03:12:00-CME-001", "CME Activity ID incorrect"
    assert example_cme["versionId"] == 2, "CME Version ID incorrect"
    assert not example_cme["cmeAnalyses"][0]["enlilList"][0]["isEarthGB"], "Nested CME values incorrect"
