import unittest

from word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.wordBreak("leetcode", ["leet", "code"]))

    def test_example_2(self):
        self.assertTrue(self.solution.wordBreak("applepenapple", ["apple", "pen"]))

    def test_example_3(self):
        self.assertFalse(self.solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_overlapping_prefixes(self):
        self.assertTrue(self.solution.wordBreak("cars", ["car", "ca", "rs"]))

    def test_many_repeats(self):
        self.assertFalse(self.solution.wordBreak("a" * 30 + "b", ["a", "aa", "aaa"]))


if __name__ == "__main__":
    unittest.main()
