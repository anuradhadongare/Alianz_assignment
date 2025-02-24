# test_hockey_stats.py
import pytest
from hockey_scraper import analyze_data  # Replace your_script_name

def test_analyze_data():
    test_data = [
        ["Team A", "1990-91", "20", "10"],
        ["Team B", "1990-91", "15", "15"],
        ["Team C", "1991-92", "25", "5"],
        ["Team D", "1991-92", "10", "20"],
        ["Team E", "1991-92", "25", "5"], # Tie for winner
    ]
    summary = analyze_data(test_data)
    expected_summary = [
        [1990, "Team A", 20, "Team B", 15],
        [1991, "Team C", 25, "Team D", 10], # Team C taken as winner
    ]
    assert summary == expected_summary

