import asyncio
import logging
from datetime import datetime

from feed_manager.match_loader import load_matches_today
from feed_manager.odds_loader import load_odds_fluctuations
from feed_manager.stats_loader import load_player_stats
from auto_gpt.core import AutoGPTCore
from utils.config import ARCAN_SHADOW_TRACKER_ENDPOINT, API_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class ArcanBetFeedOrchestrator:
    def __init__(self):
        self.auto_gpt = AutoGPTCore()
        self.poll_interval_live = 30    # seconds for live matches
        self.poll_interval_prematch = 600  # seconds for pre-match data

    async def fetch_and_process(self):
        logging.info("Starting fetch and process cycle")

        # 1. Charger les matchs du jour
        matches = await load_matches_today()
        normalized_matches = [self._normalize_match(m) for m in matches]
        logging.info(f"{len(normalized_matches)} matches du jour récupérés")

        # 2. Charger fluctuations des côtes
        odds = await load_odds_fluctuations()
        normalized_odds = [self._normalize_odds(o) for o in odds]
        logging.info(f"Données de cotes récupérées ({len(normalized_odds)} entrées)")

        # 3. Charger stats joueurs
        player_stats = await load_player_stats()
        normalized_stats = [self._normalize_player_stats(s) for s in player_stats]
        logging.info(f"Stats joueurs récupérées ({len(normalized_stats)} entrées)")

        # 4. Construire la tâche AutoGPT pour chaque match
        for match in normalized_matches:
            context = self._build_context(match, normalized_odds, normalized_stats)
            task_json = self.auto_gpt.construct_task(context)
            await self._send_to_shadow_tracker(task_json)

        logging.info("Cycle fetch and process terminé")

    def _build_context(self, match, odds, player_stats):
        relevant_odds = [o for o in odds if o['match_id'] == match['match_id']]
        relevant_stats = [s for s in player_stats if s['match_id'] == match['match_id']]

        context = {
            "match_id": match['match_id'],
            "competition": match['competition'],
            "time": datetime.utcnow().isoformat(),
            "match_data": match,
            "odds_data": relevant_odds,
            "player_stats": relevant_stats,
            "parameters": {
                "phase_lunaire": "croissante",
                "mirror_score": True,
                "line_behavior": "flat_under_pressure"
            },
            "goal": "Prédiction hybride à forte probabilité"
        }
        return context

    async def _send_to_shadow_tracker(self, task_json):
        try:
            response = await self.auto_gpt.send_task(task_json, ARCAN_SHADOW_TRACKER_ENDPOINT, API_TOKEN)
            logging.info(f"Tâche envoyée, réponse: {response.status_code}")
        except Exception as e:
            logging.error(f"Erreur en envoyant la tâche: {e}")

    def _normalize_match(self, raw):
        return {
            "id": raw.get("id") or raw.get("match_id"),
            "competition": raw.get("competition", "unknown"),
            "home_team": raw.get("home_team", "?"),
            "away_team": raw.get("away_team", "?"),
            "start_time": raw.get("start_time"),
            "match_id": raw.get("match_id") or raw.get("id")
        }

    def _normalize_odds(self, raw):
        return {
            "match_id": raw.get("match_id"),
            "bookmaker": raw.get("bookmaker"),
            "market": raw.get("market"),
            "odds": raw.get("odds")
        }

    def _normalize_player_stats(self, raw):
        return {
            "match_id": raw.get("match_id"),
            "player_id": raw.get("player_id"),
            "stats": raw.get("stats")
        }

    async def start(self):
        while True:
            try:
                await self.fetch_and_process()
                await asyncio.sleep(self.poll_interval_live)
            except Exception as e:
                logging.error(f"Erreur dans la boucle principale: {e}")
                await asyncio.sleep(60)

if __name__ == "__main__":
    orchestrator = ArcanBetFeedOrchestrator()
    asyncio.run(orchestrator.start())
