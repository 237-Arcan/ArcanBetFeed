# tests/test_feed_manager/test_filters.py

import pytest
from feed_manager.filters import detect_anomalies

def test_detect_anomalies():
    matches = [
        {"match_id": "001", "teams": "Team A vs Team B"},
        {"match_id": "002", "teams": "Team C vs Team D"}
    ]
    
    odds = {
        "001": {"home": 1.75, "draw": 3.20, "away": 4.10},
        "002": {"home": 1.25, "draw": 3.50, "away": 10.00}
    }

    result = detect_anomalies(matches, odds)

    assert isinstance(result, list)
    assert all("match_id" in match for match in result)
    assert len(result) >= 1  # au moins une anomalie détectée
