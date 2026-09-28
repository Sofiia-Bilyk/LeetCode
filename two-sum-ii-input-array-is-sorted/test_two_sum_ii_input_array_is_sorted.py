import unittest

from two_sum_ii_input_array_is_sorted import Solution


class TestTwoSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_example_2(self):
        self.assertEqual(self.solution.twoSum([2, 3, 4], 6), [1, 3])

    def test_example_3(self):
        self.assertEqual(self.solution.twoSum([-1, 0], -1), [1, 2])

    def test_duplicates(self):
        self.assertEqual(self.solution.twoSum([0, 0, 3, 4], 0), [1, 2])

    def test_pair_in_middle(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5])


if __name__ == "__main__":
    unittest.main()
