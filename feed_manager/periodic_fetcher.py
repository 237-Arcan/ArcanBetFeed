import time
import logging
from feed_manager.data_aggregator import aggregate_all_feeds

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def periodic_data_fetch(interval_seconds=600):
    """
    Fonction pour lancer l'agrégation des données toutes les `interval_seconds`.
    Exemple : interval_seconds=600 -> toutes les 10 minutes.
    """
    while True:
        try:
            logging.info("Début de l'agrégation des flux de données.")
            data = aggregate_all_feeds()
            logging.info(f"Données agrégées avec succès. Total clés récupérées : {len(data)}")
            # Ici, tu peux ajouter une sauvegarde ou traitement des données
        except Exception as e:
            logging.error(f"Erreur durant l'agrégation : {e}")

        logging.info(f"Attente de {interval_seconds} secondes avant la prochaine agrégation.")
        time.sleep(interval_seconds)
