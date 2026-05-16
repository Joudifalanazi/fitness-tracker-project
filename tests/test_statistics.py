import unittest

from statistics import (
    calculate_pace_distribution,
    calculate_performance_index
)


class TestStatistics(unittest.TestCase):

    def test_pace_distribution(self):

        result = calculate_pace_distribution(30, 5)

        self.assertEqual(result, 6.0)

    def test_performance_index(self):

        result = calculate_performance_index(300, 5)

        self.assertEqual(result, 350.0)


if __name__ == "__main__":
    unittest.main()
