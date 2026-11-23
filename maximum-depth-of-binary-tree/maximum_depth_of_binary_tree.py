from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        stack = [(root, 1)]
        while stack:
            node, node_depth = stack.pop()
            depth = max(depth, node_depth)
            if node.left is not None:
                stack.append((node.left, node_depth + 1))
            if node.right is not None:
                stack.append((node.right, node_depth + 1))

        return depth
