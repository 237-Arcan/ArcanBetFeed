

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import os
import unittest
import asyncio
from unittest.mock import AsyncMock, patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import ArcanBetFeedOrchestrator

class MockResponse:
    status_code = 200

class TestOrchestrator(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_and_process(self):
        orchestrator = ArcanBetFeedOrchestrator()

        with patch.object(orchestrator.auto_gpt, 'send_task', new=AsyncMock(return_value=MockResponse())):
            await orchestrator.fetch_and_process()
            print("✅ Test exécuté avec succès (mocked API call)")

if __name__ == "__main__":
    unittest.main()
