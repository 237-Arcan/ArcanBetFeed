# feed_manager/filters.py

def detect_anomalies(matches, odds):
    """
    Détecte des anomalies simples dans les cotes, comme des cotes home trop basses (<1.30),
    ou des écarts suspects entre home et away (>2.00).
    """
    anomalies = []

    for match in matches:
        match_id = match.get("match_id")
        match_odds = odds.get(match_id)

        if not match_odds:
            continue  # Pas de cotes dispo pour ce match

        home = match_odds.get("home")
        away = match_odds.get("away")

        if home is not None and home < 1.30:
            anomalies.append({
                "match_id": match_id,
                "type": "low_home_odds",
                "value": home,
                "reason": f"Cote home très basse ({home})"
            })

        if home is not None and away is not None:
            if abs(home - away) > 2.0:
                anomalies.append({
                    "match_id": match_id,
                    "type": "high_discrepancy",
                    "home": home,
                    "away": away,
                    "reason": f"Écart important entre cotes home ({home}) et away ({away})"
                })

    return anomalies
