# feed_manager/__init__.py

"""
feed_manager - Module de gestion des flux de données sportives et de cotes

Ce module centralise les fonctions de :
- Chargement des matchs (via fichiers issus des dépôts forkés)
- Parsing des cotes issues de dépôts GitHub
- Application de filtres avancés sur les comportements des lignes de paris

Ce package est utilisé directement par le cœur AutoGPT d'ArcanBetFeed.
"""

import logging

# Configuration du logger du feed manager
logger = logging.getLogger("feed_manager")
logger.setLevel(logging.INFO)

# Création d'un handler console si le logger n'en a pas encore
if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - FEED_MANAGER - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

# Importations clés pour rendre le module accessible en import direct
from .match_loader import load_matches_from_json, load_matches_from_csv
from .odds_parser import parse_odds_from_json, normalize_market_data
from .filters import detect_suspicious_odds, filter_by_alignment

__all__ = [
    "load_matches_from_json",
    "load_matches_from_csv",
    "parse_odds_from_json",
    "normalize_market_data",
    "detect_suspicious_odds",
    "filter_by_alignment",
    "logger"
]
