import unittest
from statistics import calculate_performance_index

class TestStatistics(unittest.TestCase):

    def test_performance_index(self):
        result = calculate_performance_index(10, 500)
        self.assertEqual(result, 50)

if __name__ == "__main__":
    unittest.main()
