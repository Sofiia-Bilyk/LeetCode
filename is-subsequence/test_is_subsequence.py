import unittest

from is_subsequence import Solution


class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))

    def test_example_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))

    def test_empty_t(self):
        self.assertFalse(self.solution.isSubsequence("a", ""))

    def test_repeated_letters(self):
        self.assertFalse(self.solution.isSubsequence("aaa", "aa"))


if __name__ == "__main__":
    unittest.main()
