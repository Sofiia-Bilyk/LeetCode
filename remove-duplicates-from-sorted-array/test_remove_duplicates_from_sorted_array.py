import unittest

from remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check(self, nums, expected):
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, len(expected))
        self.assertEqual(nums[:k], expected)

    def test_example_1(self):
        self.check([1, 1, 2], [1, 2])

    def test_example_2(self):
        self.check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])

    def test_single_element(self):
        self.check([5], [5])

    def test_no_duplicates(self):
        self.check([-3, -1, 0, 2], [-3, -1, 0, 2])


if __name__ == "__main__":
    unittest.main()
