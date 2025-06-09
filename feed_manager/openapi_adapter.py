import os
import json

class OpenAPIDirectoryParser:
    def __init__(self, base_path="data_sources/matches/openapi_directory/APIs"):
        self.base_path = base_path
        self.endpoints = {}

    def load_sport_endpoints(self):
        for root, _, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".json"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                            title = data.get("info", {}).get("title", "").lower()
                            tags = [tag.lower() for tag in data.get("tags", [])]

                            if "sport" in title or any("sport" in tag for tag in tags):
                                self.endpoints[title or file] = {
                                    "path": filepath,
                                    "raw": data
                                }

                    except json.JSONDecodeError:
                        print(f"[!] JSON invalide ignoré : {filepath}")
                    except Exception as e:
                        print(f"[!] Erreur lors du traitement de {filepath} : {e}")

        return self.endpoints

    def get_available_sports(self):
        """Retourne une liste des titres d’APIs sportives trouvées"""
        return list(self.endpoints.keys())

    def get_raw_data(self, title):
        """Retourne les données brutes d’un endpoint à partir de son titre"""
        return self.endpoints.get(title, {}).get("raw")

    def summary(self):
        """Affiche un résumé simple"""
        print(f"🔍 {len(self.endpoints)} APIs sportives détectées.")
        for title, content in self.endpoints.items():
            print(f"• {title} → {content['path']}")
