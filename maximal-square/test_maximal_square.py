import unittest

from maximal_square import Solution


class TestMaximalSquare(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [["1", "0", "1", "0", "0"],
                  ["1", "0", "1", "1", "1"],
                  ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maximalSquare([["0", "1"], ["1", "0"]]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maximalSquare([["0"]]), 0)

    def test_all_ones(self):
        self.assertEqual(self.solution.maximalSquare([["1"] * 3 for _ in range(3)]), 9)

    def test_single_row(self):
        self.assertEqual(self.solution.maximalSquare([["1", "1", "1"]]), 1)


if __name__ == "__main__":
    unittest.main()
