# feed_manager/data_aggregator.py

from feed_manager.openapi_adapter import fetch_openapi_endpoints
from feed_manager.soccerdata_adapter import fetch_soccerdata_matches
from feed_manager.sportsbetting_adapter import fetch_sportsbetting_odds
from feed_manager.bet365_adapter import fetch_bet365_odds
from feed_manager.sportsbook_adapter import fetch_sportsbook_odds
from feed_manager.whoscored_adapter import load_whoscored_player_stats

def aggregate_all_feeds():
    """
    Agrège les données des différentes sources :
    - Matchs du jour (OpenAPI & Soccerdata)
    - Fluctuations des cotes (Sportsbetting, Bet365, Sportsbook)
    - Statistiques joueurs (Whoscored)
    
    Retourne un dict avec toutes les données.
    """
    aggregated_data = {}

    # Matchs du jour
    aggregated_data['openapi_matches'] = fetch_openapi_endpoints()
    aggregated_data['soccerdata_matches'] = fetch_soccerdata_matches()

    # Cotes
    aggregated_data['sportsbetting_odds'] = fetch_sportsbetting_odds()
    aggregated_data['bet365_odds'] = fetch_bet365_odds()
    aggregated_data['sportsbook_odds'] = fetch_sportsbook_odds()

    # Stats joueurs
    aggregated_data['whoscored_stats'] = load_whoscored_player_stats()

    return aggregated_data
