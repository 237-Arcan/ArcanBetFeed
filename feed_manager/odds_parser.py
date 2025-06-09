"""
Module pour parser les fichiers de cotes et structurer les données selon les marchés et bookmakers.
"""

import pandas as pd
from typing import Dict, Any, List

def parse_odds_from_csv(file_path: str) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Parse un fichier CSV de cotes et structure les données par match et marché.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        dict: Cotes structurées {match_id: {market: [{bookmaker, odd}, ...], ...}, ...}

    Raises:
        RuntimeError: En cas d'erreur de parsing.
    """
    try:
        data = pd.read_csv(file_path)
        required_columns = {'match_id', 'bookmaker', 'market', 'odd'}
        if not required_columns.issubset(data.columns):
            missing = required_columns - set(data.columns)
            raise ValueError(f"Colonnes attendues manquantes: {missing}")
        structured_odds: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        for _, row in data.iterrows():
            match_id = str(row['match_id'])
            market = str(row['market'])
            if match_id not in structured_odds:
                structured_odds[match_id] = {}
            if market not in structured_odds[match_id]:
                structured_odds[match_id][market] = []
            structured_odds[match_id][market].append({
                "bookmaker": row['bookmaker'],
                "odd": float(row['odd'])
            })
        return structured_odds
    except Exception as e:
        raise RuntimeError(f"Erreur lors du parsing des cotes : {e}")
