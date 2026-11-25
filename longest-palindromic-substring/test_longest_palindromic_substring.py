import unittest

from longest_palindromic_substring import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertIn(self.solution.longestPalindrome("babad"), ("bab", "aba"))

    def test_example_2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_single_character(self):
        self.assertEqual(self.solution.longestPalindrome("7"), "7")

    def test_even_palindrome_at_start(self):
        self.assertEqual(self.solution.longestPalindrome("1221x"), "1221")

    def test_maximum_length(self):
        text = "a" * 1000
        self.assertEqual(self.solution.longestPalindrome(text), text)


if __name__ == "__main__":
    unittest.main()
