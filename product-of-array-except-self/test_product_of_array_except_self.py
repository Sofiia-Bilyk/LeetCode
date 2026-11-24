import unittest

from product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_2(self):
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_two_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([0, 2, 0, -3]), [0, 0, 0, 0])

    def test_two_elements(self):
        self.assertEqual(self.solution.productExceptSelf([-2, 5]), [5, -2])

    def test_zero_at_endpoint(self):
        self.assertEqual(self.solution.productExceptSelf([2, -3, 0]), [0, 0, -6])


if __name__ == "__main__":
    unittest.main()
