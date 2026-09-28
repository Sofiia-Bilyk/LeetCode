import unittest
from collections import deque

from binary_tree_level_order_traversal import Solution, TreeNode


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


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])),
                         [[3], [9, 20], [15, 7]])

    def test_example_2(self):
        self.assertEqual(self.solution.levelOrder(build_tree([1])), [[1]])

    def test_example_3(self):
        self.assertEqual(self.solution.levelOrder(build_tree([])), [])

    def test_left_skewed(self):
        self.assertEqual(self.solution.levelOrder(build_tree([1, 2, None, 3])), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
