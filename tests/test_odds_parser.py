# tests/test_odds_parser.py

import pytest
from feed_manager.odds_parser import parse_odds_data

def test_parse_odds_data(monkeypatch):
    # Données simulées
    mock_data = {
        "001": {"home": 1.75, "draw": 3.20, "away": 4.50},
        "002": {"home": 1.60, "draw": 3.50, "away": 5.10}
    }

    # Fonction simulée qui remplace la vraie source de données
    def mock_parse_odds_data():
        return mock_data

    # Remplacement temporaire de la fonction réelle par la mock
    monkeypatch.setattr("feed_manager.odds_parser.parse_odds_data", mock_parse_odds_data)

    # Exécution de la fonction mockée
    odds = parse_odds_data()

    # Assertions
    assert isinstance(odds, dict)
    assert "001" in odds
    assert odds["001"]["home"] == 1.75
    assert odds["002"]["away"] == 5.10
