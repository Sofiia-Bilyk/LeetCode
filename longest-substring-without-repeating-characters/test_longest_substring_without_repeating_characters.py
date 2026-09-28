import unittest

from longest_substring_without_repeating_characters import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_repeat_outside_window(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abba"), 2)

    def test_spaces_count(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a b c"), 3)


if __name__ == "__main__":
    unittest.main()
