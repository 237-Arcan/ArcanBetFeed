from typing import Dict, List

def apply_rules(context: Dict, betting_data: Dict) -> List[str]:
    """
    Applique les règles décisionnelles en fonction du contexte du match et des données de pari.

    Args:
        context (Dict): Informations sur le match (compétition, heure, paramètres ésotériques, etc.).
        betting_data (Dict): Données relatives aux volumes de pari et variations de cotes.

    Returns:
        List[str]: Liste des modules ArcanShadow à activer.
    """
    modules_to_activate = []

    # Règle : compétition asiatique en journée => EasternGate
    if context.get("competition", "").lower() == "championnat asiatique" and context.get("is_daytime", False):
        modules_to_activate.append("EasternGate")

    # Règle : volume sur favori > 65% + cote stable ou haussière => ShadowOdds+
    if betting_data.get("volume_favori", 0) > 65 and betting_data.get("cote_change", 0) >= 0:
        modules_to_activate.append("ShadowOdds+")

    # Règle : jour numérologique et date miroir => ChronoEcho
    if context.get("numerology_day_aligned", False) and context.get("mirror_date_present", False):
        modules_to_activate.append("ChronoEcho")

    # Règle : divergence entre XGBoost et AstroImpact => High entropy alert (module fictif)
    if context.get("xgboost_score") is not None and context.get("astro_impact_score") is not None:
        xg = context["xgboost_score"]
        astro = context["astro_impact_score"]
        if abs(xg - astro) > 0.5:
            modules_to_activate.append("HighEntropyAlert")

    return modules_to_activate
