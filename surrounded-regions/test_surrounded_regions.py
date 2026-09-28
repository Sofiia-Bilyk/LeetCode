import unittest

from surrounded_regions import Solution


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check(self, board, expected):
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_example_1(self):
        self.check([["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"]],
                   [["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"]])

    def test_example_2(self):
        self.check([["X"]], [["X"]])

    def test_region_connected_to_edge(self):
        self.check([["X", "O", "X"],
                    ["X", "O", "X"],
                    ["X", "X", "X"]],
                   [["X", "O", "X"],
                    ["X", "O", "X"],
                    ["X", "X", "X"]])

    def test_all_o(self):
        self.check([["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]])


if __name__ == "__main__":
    unittest.main()
