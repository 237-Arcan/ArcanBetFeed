# feed_manager/whoscored_adapter.py

import os
import json

WHOSCORED_DATA_PATH = "data_sources/player_stats/scraper-whoscored/data"

def load_whoscored_player_stats(file_name=None):
    """
    Charge les statistiques joueurs extraites de whoscored.
    Si file_name non spécifié, charge le fichier JSON le plus récent.

    :param file_name: nom du fichier JSON
    :return: liste ou dict des stats joueurs
    """
    if file_name is None:
        files = [f for f in os.listdir(WHOSCORED_DATA_PATH) if f.endswith(".json")]
        if not files:
            return []
        files.sort(reverse=True)
        file_name = files[0]

    file_path = os.path.join(WHOSCORED_DATA_PATH, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Erreur chargement Whoscored: {e}")
        return []

def get_player_stats(player_id):
    """
    Retourne les statistiques d'un joueur spécifique par son identifiant.

    :param player_id: identifiant du joueur
    :return: dict des stats joueur
    """
    all_stats = load_whoscored_player_stats()
    for player in all_stats:
        if player.get("player_id") == player_id:
            return player
    return {}
