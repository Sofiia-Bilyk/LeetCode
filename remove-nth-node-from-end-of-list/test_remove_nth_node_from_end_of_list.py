import unittest

from remove_nth_node_from_end_of_list import ListNode, Solution


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


class TestRemoveNthFromEnd(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check(self, values, n, expected):
        self.assertEqual(to_values(self.solution.removeNthFromEnd(build_list(values), n)), expected)

    def test_example_1(self):
        self.check([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

    def test_example_2(self):
        self.check([1], 1, [])

    def test_example_3(self):
        self.check([1, 2], 1, [1])

    def test_remove_head(self):
        self.check([1, 2, 3], 3, [2, 3])


if __name__ == "__main__":
    unittest.main()
