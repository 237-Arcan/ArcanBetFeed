"""
Initialisation du module AutoGPT Core Unit pour ArcanBetFeed.

Ce fichier configure les éléments cognitifs nécessaires à la génération de requêtes prédictives
vers le serveur ArcanShadowTracker. Il centralise l'importation des sous-composants et
prépare l’environnement AutoGPT à être piloté dynamiquement via ArcanBetFeed.
"""

# autogpt_core/__init__.py

# Ce fichier permet d'importer automatiquement les sous-modules du package autogpt_core
from .task_generator import generate_task
from .context_interpreter import interpret_context
from .rules_engine import apply_rules
from typing import Any
# Dictionnaire de routage des fonctions (utile pour orchestrateur)
auto_gpt_core = {
    "generate_task": task_generator,
    "interpreter_context": context_interpreter,
    "apply_rules": rules_engine
}

# Configuration automatique au démarrage si besoin
def init_autogpt_core(verbose: bool = False):
    if verbose:
        print("[AutoGPT Core] Initialisation du moteur cognitif...")
        print(" - Task Generator prêt")
        print(" - Context Interpreter prêt")
        print(" - Rules Engine chargé")
