import unittest

from combination_sum import Solution


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_example_2(self):
        self.assertCountEqual(
            self.solution.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        )

    def test_example_3(self):
        self.assertEqual(self.solution.combinationSum([2], 1), [])

    def test_unsorted_candidates(self):
        self.assertCountEqual(self.solution.combinationSum([5, 3, 2], 6), [[2, 2, 2], [3, 3]])

    def test_unreachable_target(self):
        self.assertEqual(self.solution.combinationSum([4, 6], 7), [])


if __name__ == "__main__":
    unittest.main()
