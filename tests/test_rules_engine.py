import unittest
from autogpt_core.rules_engine import apply_rules

class TestRulesEngine(unittest.TestCase):

    def test_apply_rules(self):
        context = {
            "competition": "championnat asiatique",
            "is_daytime": True,
            "numerology_day_aligned": True,
            "mirror_date_present": True,
            "xgboost_score": 0.8,
            "astro_impact_score": 0.1
        }
        betting_data = {
            "volume_favori": 70,
            "cote_change": 0.1
        }
        expected_modules = ["EasternGate", "ShadowOdds+", "ChronoEcho", "HighEntropyAlert"]
        result = apply_rules(context, betting_data)
        self.assertCountEqual(result, expected_modules)

if __name__ == "__main__":
    unittest.main()
