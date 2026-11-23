import unittest

from group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertCountEqual(
            [sorted(group) for group in result],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )

    def test_example_2(self):
        self.assertEqual(self.solution.groupAnagrams([""]), [[""]])

    def test_example_3(self):
        self.assertEqual(self.solution.groupAnagrams(["a"]), [["a"]])

    def test_duplicate_strings(self):
        result = self.solution.groupAnagrams(["ab", "ba", "ab", "", ""])
        self.assertCountEqual([sorted(group) for group in result], [["ab", "ab", "ba"], ["", ""]])

    def test_different_letter_counts(self):
        result = self.solution.groupAnagrams(["aab", "aba", "abb"])
        self.assertCountEqual([sorted(group) for group in result], [["aab", "aba"], ["abb"]])


if __name__ == "__main__":
    unittest.main()
