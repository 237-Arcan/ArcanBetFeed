# autogpt_core/context_interpreter.py

from typing import Dict

def interpret_context(match_info: Dict) -> Dict:
    """
    Analyse le contexte d'un match donné (ex: heure locale, compétition, phase lunaire).
    Retourne un dictionnaire des infos pertinentes.
    """
    # Extrait quelques données
    context = {}
    context['local_time'] = match_info.get('local_time')  # ex: '15:30'
    context['competition'] = match_info.get('competition')
    context['phase_lunaire'] = match_info.get('phase_lunaire', 'inconnue')
    
    # Exemple : déduire si match en journée ou soirée
    hour = int(context['local_time'].split(':')[0]) if context['local_time'] else 0
    context['is_daytime'] = 6 <= hour < 18
    
    return context
