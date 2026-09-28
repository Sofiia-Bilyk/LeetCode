from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node.left is not None:
                last = dfs(node.left)
                node.left = None
                right = node.right
                node.right = last
                check_lat = last
                while check_lat.right:
                    check_lat.left = None
                    check_lat = check_lat.right
                check_lat.right = right
            if node.right is not None:
                dfs(node.right)
            return node

        if not root:
            return root

        res = dfs(root)
