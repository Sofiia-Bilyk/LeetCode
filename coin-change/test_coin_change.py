import unittest

from coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)

    def test_greedy_fails(self):
        self.assertEqual(self.solution.coinChange([1, 3, 4], 6), 2)

    def test_unsorted_coins(self):
        self.assertEqual(self.solution.coinChange([186, 419, 83, 408], 6249), 20)


if __name__ == "__main__":
    unittest.main()
