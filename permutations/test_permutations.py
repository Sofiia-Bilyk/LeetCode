import unittest
from itertools import permutations

from permutations import Solution


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(
            self.solution.permute([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )

    def test_example_2(self):
        self.assertCountEqual(self.solution.permute([0, 1]), [[0, 1], [1, 0]])

    def test_example_3(self):
        self.assertEqual(self.solution.permute([1]), [[1]])

    def test_maximum_length(self):
        nums = [-10, 3, 0, -2, 10, 5]
        result = self.solution.permute(nums)
        self.assertCountEqual([tuple(order) for order in result], permutations(nums))

    def test_preserves_input_order(self):
        nums = [3, -2, 0]
        self.solution.permute(nums)
        self.assertEqual(nums, [3, -2, 0])


if __name__ == "__main__":
    unittest.main()
