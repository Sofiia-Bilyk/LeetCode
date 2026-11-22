import unittest

from text_justification import Solution


class TestTextJustification(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        expected = ["This    is    an", "example  of text", "justification.  "]
        self.assertEqual(self.solution.fullJustify(words, 16), expected)

    def test_example_2(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        expected = ["What   must   be", "acknowledgment  ", "shall be        "]
        self.assertEqual(self.solution.fullJustify(words, 16), expected)

    def test_example_3(self):
        words = "Science is what we understand well enough to explain to a computer. Art is everything else we do".split()
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        self.assertEqual(self.solution.fullJustify(words, 20), expected)

    def test_exact_width_word(self):
        self.assertEqual(self.solution.fullJustify(["abcd", "x"], 4), ["abcd", "x   "])

    def test_single_line_with_multiple_words(self):
        self.assertEqual(self.solution.fullJustify(["a", "b"], 5), ["a b  "])


if __name__ == "__main__":
    unittest.main()
