import unittest

from maximum_average_subarray_i import Solution


class TestFindMaxAverage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.findMaxAverage([5], 1), 5.0)

    def test_window_is_whole_array(self):
        self.assertAlmostEqual(self.solution.findMaxAverage([1, 2, 3], 3), 2.0)

    def test_all_negative(self):
        self.assertAlmostEqual(self.solution.findMaxAverage([-1, -12, -5, -6], 2), -5.5)


if __name__ == "__main__":
    unittest.main()
