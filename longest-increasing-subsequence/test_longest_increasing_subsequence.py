import unittest

from longest_increasing_subsequence import Solution


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.lengthOfLIS([1]), 1)

    def test_strictly_decreasing(self):
        self.assertEqual(self.solution.lengthOfLIS([5, 4, 3, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
