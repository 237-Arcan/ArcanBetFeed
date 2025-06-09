import unittest
from autogpt_core.context_interpreter import interpret_context

class TestContextInterpreter(unittest.TestCase):
    def test_interpret_context_daytime(self):
        match_info = {
            "local_time": "14:30",
            "competition": "Ligue asiatique",
            "phase_lunaire": "croissante"
        }
        context = interpret_context(match_info)
        self.assertTrue(context['is_daytime'])
        self.assertEqual(context['phase_lunaire'], "croissante")

if __name__ == '__main__':
    unittest.main()
