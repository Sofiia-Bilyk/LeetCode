import unittest

from search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.search([1], 0), -1)

    def test_not_rotated(self):
        self.assertEqual(self.solution.search([1, 3, 5, 7, 9], 7), 3)

    def test_every_position(self):
        nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        for index, target in enumerate(nums):
            with self.subTest(target=target):
                self.assertEqual(self.solution.search(nums, target), index)


if __name__ == "__main__":
    unittest.main()
