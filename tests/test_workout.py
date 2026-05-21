import unittest
from workout import create_workout

class TestWorkout(unittest.TestCase):

    def test_create_workout(self):

        workout = create_workout(
            "2026-05-16",
            "Running",
            30,
            5,
            300,
            145
        )

        self.assertEqual(workout["exercise_type"], "Running")
        self.assertEqual(workout["duration_minutes"], 30)
return workout

if __name__ == "__main__":
    unittest.main()
