# feed_manager/soccerdata_adapter.py

import os
import pandas as pd
from datetime import datetime

SOCCERDATA_PATH = "data_sources/matches/soccerdata/data"

def get_today_matches(leagues=None):
    """
    Extrait les matchs du jour à partir des fichiers CSV de Soccerdata.
    
    :param leagues: Liste optionnelle de ligues (ex: ['EPL', 'SPA', 'ITA'])
    :return: Liste de dictionnaires de matchs
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    matches_today = []

    leagues = leagues or os.listdir(SOCCERDATA_PATH)

    for league in leagues:
        league_path = os.path.join(SOCCERDATA_PATH, league, "matches.csv")
        if not os.path.exists(league_path):
            continue

        try:
            df = pd.read_csv(league_path, parse_dates=['date'])
            df_today = df[df['date'] == today_str]

            for _, row in df_today.iterrows():
                match = {
                    "league": league,
                    "date": row["date"].strftime("%Y-%m-%d"),
                    "home_team": row["home_team"],
                    "away_team": row["away_team"],
                    "score": row.get("score", None),
                    "match_id": f"{league}_{row['home_team']}_vs_{row['away_team']}"
                }
                matches_today.append(match)
        except Exception as e:
            print(f"Erreur lecture {league_path}: {e}")
            continue

    return matches_today
