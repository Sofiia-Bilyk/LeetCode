import unittest

from find_minimum_in_rotated_sorted_array import Solution


class TestFindMin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMin([3, 4, 5, 1, 2]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.findMin([11, 13, 15, 17]), 11)

    def test_two_elements(self):
        self.assertEqual(self.solution.findMin([2, 1]), 1)

    def test_every_rotation(self):
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8]
        for shift in range(len(sorted_nums)):
            nums = sorted_nums[shift:] + sorted_nums[:shift]
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.findMin(nums), 1)


if __name__ == "__main__":
    unittest.main()
