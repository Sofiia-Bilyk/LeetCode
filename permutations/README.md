# 46. Permutations

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/permutations/description/

Given an array `nums` of distinct integers, return every arrangement that uses each integer exactly once. The permutations may be returned in any order.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```

**Constraints:**

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All values in `nums` are distinct.

**Approach**

Backtrack over a copy of the input. Swap each remaining value into the current position, recurse to fill the next position, then undo the swap. Save a copy of each completed permutation. This takes O(n × n!) time and O(n) auxiliary space, excluding the output.
