"""
Module pour charger les données de matchs depuis des fichiers CSV ou JSON.
"""

import os
import pandas as pd
import json
from typing import Union, Dict, Any

def load_match_data_from_csv(file_path: str) -> pd.DataFrame:
    """
    Charge les données de matchs depuis un fichier CSV.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        pd.DataFrame: Données du fichier CSV.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        pd.errors.EmptyDataError: Si le fichier est vide.
        pd.errors.ParserError: Si le fichier est mal formé.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Fichier CSV introuvable: {file_path}")
    return pd.read_csv(file_path)

def load_match_data_from_json(file_path: str) -> Union[Dict[str, Any], pd.DataFrame]:
    """
    Charge les données de matchs depuis un fichier JSON.

    Args:
        file_path (str): Chemin du fichier JSON.

    Returns:
        dict ou pd.DataFrame: Données extraites du fichier JSON.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        json.JSONDecodeError: Si le contenu JSON est invalide.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Fichier JSON introuvable: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Retourner un DataFrame si le JSON contient une liste d'objets
        if isinstance(data, list):
            return pd.DataFrame(data)
        return data
