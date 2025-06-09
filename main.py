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
        logging.info(f"{len(matches)} matches du jour récupérés")

        # 2. Charger fluctuations des côtes
        odds = await load_odds_fluctuations()
        logging.info(f"Données de cotes récupérées ({len(odds)} entrées)")

        # 3. Charger stats joueurs
        player_stats = await load_player_stats()
        logging.info(f"Stats joueurs récupérées ({len(player_stats)} entrées)")

        # 4. Construire la tâche AutoGPT pour chaque match
        for match in matches:
            context = self._build_context(match, odds, player_stats)
            task_json = self.auto_gpt.construct_task(context)
            await self._send_to_shadow_tracker(task_json)

        logging.info("Cycle fetch and process terminé")

    def _build_context(self, match, odds, player_stats):
        # Construit le contexte d'analyse combiné pour AutoGPT
        # Exemple simplifié, à étendre selon besoin
        relevant_odds = [o for o in odds if o['match_id'] == match['id']]
        relevant_stats = [s for s in player_stats if s['match_id'] == match['id']]

        context = {
            "match_id": match['id'],
            "competition": match['competition'],
            "time": datetime.utcnow().isoformat(),
            "match_data": match,
            "odds_data": relevant_odds,
            "player_stats": relevant_stats,
            "parameters": {
                "phase_lunaire": "croissante",  # placeholder, à calculer dynamiquement
                "mirror_score": True,
                "line_behavior": "flat_under_pressure"
            },
            "goal": "Prédiction hybride à forte probabilité"
        }
        return context

    async def _send_to_shadow_tracker(self, task_json):
        # Envoi via webhook REST à ArcanShadowTracker
        try:
            response = await self.auto_gpt.send_task(task_json, ARCAN_SHADOW_TRACKER_ENDPOINT, API_TOKEN)
            logging.info(f"Tâche envoyée, réponse: {response.status_code}")
        except Exception as e:
            logging.error(f"Erreur en envoyant la tâche: {e}")

    async def start(self):
        while True:
            try:
                await self.fetch_and_process()
                await asyncio.sleep(self.poll_interval_live)
            except Exception as e:
                logging.error(f"Erreur dans la boucle principale: {e}")
                await asyncio.sleep(60)  # Attendre avant retry


if __name__ == "__main__":
    orchestrator = ArcanBetFeedOrchestrator()
    asyncio.run(orchestrator.start())
