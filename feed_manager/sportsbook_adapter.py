# feed_manager/sportsbook_adapter.py

import os
import json

SPORTSBOOK_DATA_PATH = "data_sources/odds/SportsBook/data"

def load_sportsbook_data(file_name=None):
    """
    Charge les données des cotes SportsBook depuis un fichier JSON.
    Si file_name non précisé, charge le fichier le plus récent.

    :param file_name: nom du fichier JSON
    :return: liste de cotes sous forme de dictionnaires
    """
    if file_name is None:
        files = [f for f in os.listdir(SPORTSBOOK_DATA_PATH) if f.endswith(".json")]
        if not files:
            return []
        files.sort(reverse=True)
        file_name = files[0]

    file_path = os.path.join(SPORTSBOOK_DATA_PATH, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur chargement cotes SportsBook: {e}")
        return []

def get_odds_by_match(match_id):
    """
    Recherche les cotes associées à un match donné.

    :param match_id: identifiant du match
    :return: dict des cotes
    """
    all_odds = load_sportsbook_data()
    for match_odds in all_odds:
        if match_odds.get("match_id") == match_id:
            return match_odds.get("odds", {})
    return {}
