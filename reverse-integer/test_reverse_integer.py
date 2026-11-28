import unittest

from reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_example_2(self):
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_example_3(self):
        self.assertEqual(self.solution.reverse(120), 21)

    def test_zero(self):
        self.assertEqual(self.solution.reverse(0), 0)

    def test_overflow(self):
        for value in (1_534_236_469, -1_563_847_412, 2_147_483_647, -2_147_483_648):
            with self.subTest(value=value):
                self.assertEqual(self.solution.reverse(value), 0)

    def test_valid_results_near_limits(self):
        self.assertEqual(self.solution.reverse(1_463_847_412), 2_147_483_641)
        self.assertEqual(self.solution.reverse(-1_463_847_412), -2_147_483_641)


if __name__ == "__main__":
    unittest.main()
