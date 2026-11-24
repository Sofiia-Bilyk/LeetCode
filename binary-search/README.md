# 704. Binary Search

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/binary-search/description/

Given an ascending array `nums` of distinct integers, return the index of `target` if present. Otherwise, return `-1`. The search must run in O(log n) time.

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- The values in `nums` are distinct and sorted in ascending order.

**Approach**

Keep an inclusive range of candidate indices. Compare the midpoint value with the target and discard the midpoint and the half that cannot contain the target. Continue until a match is found or the range is empty. This takes O(log n) time and O(1) auxiliary space.
