import unittest

from house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_single_house(self):
        self.assertEqual(self.solution.rob([400]), 400)

    def test_can_choose_both_ends(self):
        self.assertEqual(self.solution.rob([2, 1, 1, 2]), 4)

    def test_all_zero_amounts(self):
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
