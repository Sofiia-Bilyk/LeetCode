import unittest

from spiral_matrix import Solution


class TestSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_example_2(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def test_single_row(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3]]), [1, 2, 3])

    def test_single_column(self):
        self.assertEqual(self.solution.spiralOrder([[1], [2], [3]]), [1, 2, 3])

    def test_four_by_four(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(self.solution.spiralOrder(matrix),
                         [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])


if __name__ == "__main__":
    unittest.main()
