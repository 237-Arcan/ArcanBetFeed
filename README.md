ArcanBetFeed

ArcanBetFeed est un orchestrateur modulaire de collecte, normalisation et traitement de flux de données pour les prédictions hybrides de paris sportifs. Il constitue un maillon fondamental du système plus large ShadowMerge+, qui combine statistiques, comportements de cotes (ShadowOdds), signaux live (ArcanSentinel) et modèles d'analyse automatique (AutoGPT).


---

🌐 Objectif du projet

Centraliser et traiter des données pertinentes (matchs, cotes, stats joueurs) en temps réel ou pré-match pour alimenter des modules de prédiction automatique tels que ArcanShadowTracker, en utilisant une logique combinée :

Statistiques classiques (xG, forme, etc.)

Analyse du comportement des cotes (ShadowOdds)

Insights humains ou systémiques



---

📊 Architecture générale du projet

ArcanBetFeed/
├── main.py                        # Orchestrateur principal
├── feed_manager/                 # Modules de chargement des données
│   ├── match_loader.py           # Chargement des matchs du jour
│   ├── odds_loader.py            # Récupération des fluctuations de cotes
│   └── stats_loader.py           # Stats joueurs (WhoScored, etc.)
├── data_sources/                 # Référentiels GitHub clonés (soccerdata, bet365-scraper...)
├── auto_gpt/                     # Noyau logique d'AutoGPTCore (analyse de contexte)
├── utils/
│   └── config.py                 # Variables d'environnement et endpoints
├── requirements.txt             # Dépendances Python
└── README.md                    # Ce fichier


---

🚀 Sources de données intégrées

Matchs du jour

openapi-directory

soccerdata


Fluctuations des cotes

bet365-scraper

SportsBook

Sports-betting


Statistiques des joueurs

scraper-whoscored



---

⚙️ Fonctionnement

Lancement du cycle automatique de traitement via main.py :

1. Chargement des données depuis les adaptateurs de feed_manager/


2. Normalisation des structures hétérogènes (matchs, cotes, stats)


3. Construction de contexte (format JSON enrichi) par match


4. Transmission à ArcanShadowTracker pour analyse et stockage




---

🚧 Installation & Lancement

Prérequis

Python 3.10+

Git, pip


Etapes

# 1. Clone du projet
$ git clone https://github.com/237-Arcan/ArcanBetFeed.git
$ cd ArcanBetFeed

# 2. Installation des dépendances
$ pip install -r requirements.txt

# 3. Configuration des variables (API_TOKEN, endpoint, etc.)
$ cp .env.example .env
# → remplir manuellement les valeurs dans .env

# 4. Lancement
$ python main.py


---

🔄 Roadmap …

[ ] Forkage et intégration dynamique des dépôts sources

[ ] Intégration de ShadowOdds (évolution de TriggerSet)

[ ] Détection live via ArcanSentinel (signaux minute par minute)

[ ] Scheduling GitHub Actions / CronJob



---

👨‍💼 Auteurs

Projet initié et maintenu par @237-Arcan

Contributions bienvenues via issues, discussions ou PR


---

Licence : Tous droits reservés

