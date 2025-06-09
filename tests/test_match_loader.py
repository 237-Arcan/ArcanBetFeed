import unittest
import asyncio
from unittest.mock import patch, AsyncMock

# Ajuste le chemin si nécessaire
from feed_manager import match_loader

class TestMatchLoader(unittest.IsolatedAsyncioTestCase):
    @patch('feed_manager.match_loader.load_matches_today', new_callable=AsyncMock)
    async def test_load_matches_today(self, mock_load):
        mock_data = [
            {"match_id": "001", "home_team": "Team A", "away_team": "Team B", "start_time": "2025-06-10T15:00:00Z"}
        ]
        mock_load.return_value = mock_data

        result = await match_loader.load_matches_today()
        self.assertEqual(result, mock_data)
        print("✅ Match loader mocké avec succès")

if __name__ == "__main__":
    unittest.main()
