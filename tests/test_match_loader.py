# tests/test_feed_manager/test_match_loader.py

import pytest
from feed_manager.match_loader import load_today_matches

def test_load_today_matches(monkeypatch):
    mock_data = [
        {"match_id": "001", "teams": "Team A vs Team B", "date": "2025-06-08"},
        {"match_id": "002", "teams": "Team C vs Team D", "date": "2025-06-08"}
    ]

    monkeypatch.setattr("feed_manager.match_loader._read_json_or_csv", lambda: mock_data)
    
    matches = load_today_matches()
    
    assert isinstance(matches, list)
    assert all("match_id" in match for match in matches)
    assert matches[0]["match_id"] == "001"
