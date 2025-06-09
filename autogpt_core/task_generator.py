# autogpt_core/task_generator.py

from typing import List, Dict

def generate_task(match_id: str, modules: List[str], parameters: Dict, goal: str) -> Dict:
    """
    Génère une tâche prédictive à envoyer à ArcanShadowTracker.

    Args:
        match_id (str): Identifiant unique du match.
        modules (List[str]): Liste des modules ArcanShadow à activer.
        parameters (Dict): Paramètres spécifiques pour la tâche (ex: phase lunaire, comportements).
        goal (str): Objectif de la prédiction (ex: "But tardif").

    Returns:
        Dict: Tâche structurée au format JSON/dict.
    """
    task = {
        "match_id": match_id,
        "modules": modules,
        "parameters": parameters,
        "goal": goal
    }
    return task
