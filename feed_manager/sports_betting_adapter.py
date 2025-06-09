# feed_manager/sports_betting_adapter.py

import os
import json

SPORTS_BETTING_DATA_PATH = "data_sources/odds/Sports-betting/data"

def load_sports_betting_data(file_name=None):
    """
    Charge les données du dépôt Sports-betting (pretrehr).
    Si file_name non spécifié, charge le fichier JSON le plus récent.

    :param file_name: nom du fichier JSON
    :return: liste ou dict des données
    """
    if file_name is None:
        files = [f for f in os.listdir(SPORTS_BETTING_DATA_PATH) if f.endswith(".json")]
        if not files:
            return []
        files.sort(reverse=True)
        file_name = files[0]

    file_path = os.path.join(SPORTS_BETTING_DATA_PATH, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur chargement Sports-betting: {e}")
        return []

def get_odds_for_match(match_id):
    """
    Retourne les données des cotes pour un match spécifique.

    :param match_id: identifiant du match
    :return: dict des cotes
    """
    all_data = load_sports_betting_data()
    for item in all_data:
        if item.get("match_id") == match_id:
            return item.get("odds", {})
    return {}
