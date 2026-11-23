import unittest

from maximum_depth_of_binary_tree import Solution, TreeNode


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_example_2(self):
        root = TreeNode(1, right=TreeNode(2))
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(self.solution.maxDepth(TreeNode()), 1)

    def test_maximum_length_chain(self):
        root = TreeNode()
        for _ in range(9_999):
            root = TreeNode(left=root)
        self.assertEqual(self.solution.maxDepth(root), 10_000)


if __name__ == "__main__":
    unittest.main()
