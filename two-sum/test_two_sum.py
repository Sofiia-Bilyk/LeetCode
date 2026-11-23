import unittest

from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertCountEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertCountEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_negative_target(self):
        self.assertCountEqual(self.solution.twoSum([-4, 5, -2, 8], -6), [0, 2])

    def test_zero_target(self):
        self.assertCountEqual(self.solution.twoSum([0, 3, -3], 0), [1, 2])


if __name__ == "__main__":
    unittest.main()
