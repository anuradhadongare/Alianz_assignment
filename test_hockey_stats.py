# test_hockey_stats.py The pytest unit tests
#Imports the pytest library, which is the testing framework.
# Imports the analyze_data function from your hockey_scraper.py file 
import pytest
from hockey_scraper import analyze_data  # Replace your_script_name

#Defines the test function. pytest automatically recognizes functions that start with test_ as test cases.
def test_analyze_data():
    #: This is the input data for the analyze_data function. It's a list of lists, mimicking the structure of the scraped data.
    test_data = [
        ["Team A", "1990-91", "20", "10"],
        ["Team B", "1990-91", "15", "15"],
        ["Team C", "1991-92", "25", "5"],
        ["Team D", "1991-92", "10", "20"],
        ["Team E", "1991-92", "25", "15"], 
    ]
    summary = analyze_data(test_data)  #Calls the analyze_data function with the test data.
    #this is the expected output of the analyze_data function for the given test_data.
    expected_summary = [
        [1990, "Team A", 20, "Team B", 15],
        [1991, "Team C", 25, "Team D", 10], 
    ]
    #This is the assertion. It checks if the actual output (summary) matches the expected output (expected_summary). If they are equal, the test passes; otherwise, it fails.
    assert summary == expected_summary

