import unittest
from collections import deque

from binary_tree_zigzag_level_order_traversal import Solution, TreeNode


def build_tree(values):
    """Build a tree from LeetCode's level-order list, e.g. [3,9,20,None,None,15,7]."""
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


class TestZigzagLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.zigzagLevelOrder(build_tree([3, 9, 20, None, None, 15, 7])),
                         [[3], [20, 9], [15, 7]])

    def test_example_2(self):
        self.assertEqual(self.solution.zigzagLevelOrder(build_tree([1])), [[1]])

    def test_example_3(self):
        self.assertEqual(self.solution.zigzagLevelOrder(build_tree([])), [])

    def test_four_levels(self):
        tree = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(self.solution.zigzagLevelOrder(tree),
                         [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]])

    def test_uneven_tree(self):
        tree = build_tree([1, 2, 3, 4, None, None, 5])
        self.assertEqual(self.solution.zigzagLevelOrder(tree), [[1], [3, 2], [4, 5]])


if __name__ == "__main__":
    unittest.main()
