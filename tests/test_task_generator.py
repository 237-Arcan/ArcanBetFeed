import unittest
from autogpt_core.task_generator import generate_task

class TestTaskGenerator(unittest.TestCase):

    def test_generate_task(self):
        match_id = "12345"
        modules = ["ShadowOdds"]
        parameters = {"phase_lunaire": "croissante"}
        goal = "But tardif"

        task = generate_task(match_id, modules, parameters, goal)

        self.assertIsInstance(task, dict)
        self.assertEqual(task["match_id"], match_id)
        self.assertEqual(task["modules"], modules)
        self.assertEqual(task["parameters"], parameters)
        self.assertEqual(task["goal"], goal)

if __name__ == "__main__":
    unittest.main()
