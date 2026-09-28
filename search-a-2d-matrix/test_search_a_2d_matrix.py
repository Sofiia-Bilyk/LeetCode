import unittest

from search_a_2d_matrix import Solution


MATRIX = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.searchMatrix(MATRIX, 3))

    def test_example_2(self):
        self.assertFalse(self.solution.searchMatrix(MATRIX, 13))

    def test_every_value_is_found(self):
        for row in MATRIX:
            for target in row:
                with self.subTest(target=target):
                    self.assertTrue(self.solution.searchMatrix(MATRIX, target))

    def test_out_of_range(self):
        self.assertFalse(self.solution.searchMatrix(MATRIX, 0))
        self.assertFalse(self.solution.searchMatrix(MATRIX, 61))

    def test_single_cell(self):
        self.assertTrue(self.solution.searchMatrix([[1]], 1))


if __name__ == "__main__":
    unittest.main()
