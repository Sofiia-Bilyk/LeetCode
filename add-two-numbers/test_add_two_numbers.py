import unittest

from add_two_numbers import ListNode, Solution


def build_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check(self, l1, l2, expected):
        result = self.solution.addTwoNumbers(build_list(l1), build_list(l2))
        self.assertEqual(to_values(result), expected)

    def test_example_1(self):
        self.check([2, 4, 3], [5, 6, 4], [7, 0, 8])

    def test_example_2(self):
        self.check([0], [0], [0])

    def test_example_3(self):
        self.check([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])

    def test_carry_creates_new_digit(self):
        self.check([5], [5], [0, 1])

    def test_different_lengths(self):
        self.check([1], [9, 9], [0, 0, 1])


if __name__ == "__main__":
    unittest.main()
