import unittest

from valid_palindrome import Solution


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_example_3(self):
        self.assertTrue(self.solution.isPalindrome(" "))

    def test_digits_are_kept(self):
        self.assertFalse(self.solution.isPalindrome("0P"))

    def test_odd_length(self):
        self.assertTrue(self.solution.isPalindrome("No 'x' in Nixon"))


if __name__ == "__main__":
    unittest.main()
