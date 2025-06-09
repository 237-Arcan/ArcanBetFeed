import asyncio
from unittest.mock import AsyncMock, patch
from main import ArcanBetFeedOrchestrator

async def run_test():
    orchestrator = ArcanBetFeedOrchestrator()

    # Mock la méthode d'envoi vers le ShadowTracker
    with patch.object(orchestrator.auto_gpt, 'send_task', new=AsyncMock(return_value=MockResponse())):
        await orchestrator.fetch_and_process()
        print("Test exécuté avec succès (mocked API call)")

class MockResponse:
    status_code = 200

if __name__ == "__main__":
    asyncio.run(run_test())
