import sys
import os
import unittest
import asyncio
from unittest.mock import AsyncMock, patch

# 🔧 S'assurer que le dossier racine (celui contenant main.py) est dans le PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import ArcanBetFeedOrchestrator

class MockResponse:
    status_code = 200

class TestOrchestrator(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_and_process(self):
        orchestrator = ArcanBetFeedOrchestrator()

        # Mock des appels réseau pour éviter les vraies requêtes HTTP
        with patch.object(orchestrator.auto_gpt, 'send_task', new=AsyncMock(return_value=MockResponse())):
            await orchestrator.fetch_and_process()
            print("✅ Test exécuté avec succès (appel API simulé)")

if __name__ == "__main__":
    unittest.main()
