import unittest

from container_with_most_water import Solution


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_example_2(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_increasing(self):
        self.assertEqual(self.solution.maxArea([1, 2, 3, 4, 5]), 6)

    def test_equal_walls(self):
        self.assertEqual(self.solution.maxArea([4, 3, 2, 1, 4]), 16)

    def test_tall_edges(self):
        self.assertEqual(self.solution.maxArea([10, 1, 1, 1, 10]), 40)


if __name__ == "__main__":
    unittest.main()
