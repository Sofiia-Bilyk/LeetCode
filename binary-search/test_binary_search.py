import unittest

from binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_endpoints(self):
        nums = [-5, 0, 4, 10]
        self.assertEqual(self.solution.search(nums, -5), 0)
        self.assertEqual(self.solution.search(nums, 10), 3)

    def test_interior_match_after_bounds_meet(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5, 6], 4), 3)

    def test_single_element(self):
        self.assertEqual(self.solution.search([4], 4), 0)
        self.assertEqual(self.solution.search([4], 3), -1)


if __name__ == "__main__":
    unittest.main()
