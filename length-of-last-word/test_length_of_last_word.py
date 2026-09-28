import unittest

from length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("a"), 1)

    def test_single_word_with_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("  day  "), 3)


if __name__ == "__main__":
    unittest.main()
