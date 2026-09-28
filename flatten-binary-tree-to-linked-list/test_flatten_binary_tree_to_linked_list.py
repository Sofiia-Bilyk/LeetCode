import unittest
from collections import deque

from flatten_binary_tree_to_linked_list import Solution, TreeNode


def build_tree(values):
    """Build a tree from LeetCode's level-order list, e.g. [1,2,5,3,4,None,6]."""
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def flattened_values(root):
    """Walk the right pointers, checking every left pointer is None."""
    values = []
    while root:
        assert root.left is None
        values.append(root.val)
        root = root.right
    return values


class TestFlatten(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def check(self, values, expected):
        root = build_tree(values)
        self.solution.flatten(root)
        self.assertEqual(flattened_values(root), expected)

    def test_example_1(self):
        self.check([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6])

    def test_example_2(self):
        self.check([], [])

    def test_example_3(self):
        self.check([0], [0])

    def test_left_only_chain(self):
        self.check([1, 2, None, 3], [1, 2, 3])

    def test_deep_left_subtree(self):
        self.check([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7])


if __name__ == "__main__":
    unittest.main()
