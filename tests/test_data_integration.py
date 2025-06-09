import asyncio
import logging
from feed_manager.match_loader import load_matches_today
from feed_manager.odds_loader import load_odds_fluctuations
from feed_manager.stats_loader import load_player_stats

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def normalize_match(raw):
    return {
        "id": raw.get("id") or raw.get("match_id"),
        "competition": raw.get("competition", "unknown"),
        "home_team": raw.get("home_team", "?"),
        "away_team": raw.get("away_team", "?"),
        "start_time": raw.get("start_time"),
        "match_id": raw.get("match_id") or raw.get("id")
    }


def normalize_odds(raw):
    return {
        "match_id": raw.get("match_id"),
        "bookmaker": raw.get("bookmaker"),
        "market": raw.get("market"),
        "odds": raw.get("odds")
    }


def normalize_player_stats(raw):
    return {
        "match_id": raw.get("match_id"),
        "player_id": raw.get("player_id"),
        "stats": raw.get("stats")
    }


def build_context(match, odds, player_stats):
    relevant_odds = [o for o in odds if o['match_id'] == match['match_id']]
    relevant_stats = [s for s in player_stats if s['match_id'] == match['match_id']]
    context = {
        "match_id": match['match_id'],
        "competition": match['competition'],
        "match_data": match,
        "odds_data": relevant_odds,
        "player_stats": relevant_stats,
        "goal": "Test prédiction hybride"
    }
    return context


async def run_test():
    try:
        logging.info("Chargement des matchs...")
        matches = await load_matches_today()
        normalized_matches = [normalize_match(m) for m in matches]
        logging.info(f"{len(normalized_matches)} matchs chargés et normalisés.")
    except Exception as e:
        logging.error(f"Erreur lors du chargement ou de la normalisation des matchs : {e}")
        return

    try:
        logging.info("Chargement des côtes...")
        odds = await load_odds_fluctuations()
        normalized_odds = [normalize_odds(o) for o in odds]
        logging.info(f"{len(normalized_odds)} côtes chargées et normalisées.")
    except Exception as e:
        logging.error(f"Erreur lors du chargement ou de la normalisation des côtes : {e}")
        return

    try:
        logging.info("Chargement des stats joueurs...")
        stats = await load_player_stats()
        normalized_stats = [normalize_player_stats(s) for s in stats]
        logging.info(f"{len(normalized_stats)} stats joueurs chargées et normalisées.")
    except Exception as e:
        logging.error(f"Erreur lors du chargement ou de la normalisation des stats joueurs : {e}")
        return

    if not normalized_matches:
        logging.warning("Aucun match chargé, test arrêté.")
        return

    try:
        context = build_context(normalized_matches[0], normalized_odds, normalized_stats)
        logging.info("Contexte construit pour le premier match :")
        logging.info(context)
    except Exception as e:
        logging.error(f"Erreur lors de la construction du contexte : {e}")


if __name__ == "__main__":
    asyncio.run(run_test())
