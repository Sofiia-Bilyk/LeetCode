import unittest

from three_sum import Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertCountEqual([sorted(triplet) for triplet in result], [[-1, -1, 2], [-1, 0, 1]])

    def test_example_2(self):
        self.assertEqual(self.solution.threeSum([0, 1, 1]), [])

    def test_example_3(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_repeated_values(self):
        result = self.solution.threeSum([-2, 0, 0, 1, 1, 2, 2])
        self.assertCountEqual([sorted(triplet) for triplet in result], [[-2, 0, 2], [-2, 1, 1]])

    def test_preserves_input_order(self):
        nums = [1, -1, 0]
        self.solution.threeSum(nums)
        self.assertEqual(nums, [1, -1, 0])


if __name__ == "__main__":
    unittest.main()
