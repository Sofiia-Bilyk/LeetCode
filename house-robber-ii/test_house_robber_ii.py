import unittest

from house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rob([2, 3, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.rob([1, 2, 3]), 3)

    def test_single_house(self):
        self.assertEqual(self.solution.rob([7]), 7)

    def test_longer_circle(self):
        self.assertEqual(self.solution.rob([200, 3, 140, 20, 10]), 340)


if __name__ == "__main__":
    unittest.main()
