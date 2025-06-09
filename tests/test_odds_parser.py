# tests/test_feed_manager/test_odds_parser.py

import pytest
from feed_manager.odds_parser import parse_odds_data

def test_parse_odds_data(monkeypatch):
    mock_data = {
        "001": {"home": 1.75, "draw": 3.20, "away": 4.10},
        "002": {"home": 1.60, "draw": 3.50, "away": 5.00}
    }

    monkeypatch.setattr("feed_manager.odds_parser._load_odds_file", lambda: mock_data)
    
    odds = parse_odds_data()
    
    assert isinstance(odds, dict)
    assert "001" in odds
    assert odds["001"]["home"] == 1.75
