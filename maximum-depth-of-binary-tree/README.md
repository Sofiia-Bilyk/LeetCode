# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return the number of nodes on its longest root-to-leaf path. An empty tree has depth zero.

**Example 1:**

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Constraints:**

- The tree contains between 0 and `10^4` nodes.
- `-100 <= Node.val <= 100`

**Approach**

Use iterative depth-first search with a stack that stores each pending node and its depth. Start at depth one and track the greatest depth visited. The explicit stack lets the search handle a chain of 10,000 nodes within Python's recursion limit. The algorithm takes O(n) time and O(h) auxiliary space, where h is the tree height.
