"""
Module pour détecter les comportements anormaux dans les fluctuations de cotes.
"""

from typing import Dict, List, Any

def detect_suspicious_odds_behavior(
    odds_data: Dict[str, Dict[str, List[Dict[str, Any]]]], 
    threshold: float = 1.0
) -> List[str]:
    """
    Détecte les matchs présentant un comportement de cotes suspect basé sur un seuil d'écart.

    Args:
        odds_data (dict): Dictionnaire structuré des cotes.
        threshold (float): Seuil d'écart autorisé avant de signaler une anomalie.

    Returns:
        list: Liste des match_id suspects.
    """
    suspicious_matches = []
    for match_id, markets in odds_data.items():
        for market, odds in markets.items():
            if len(odds) < 2:
                continue
            odds_values = [float(o['odd']) for o in odds]
            if max(odds_values) - min(odds_values) > threshold:
                suspicious_matches.append(match_id)
                break
    return suspicious_matches
