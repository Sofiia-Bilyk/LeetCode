# 198. House Robber

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/house-robber/description/

Given an integer array `nums` of amounts in houses along a street, return the largest total obtainable by choosing houses with no two adjacent.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 4
```

**Example 2:**

```
Input: nums = [2,7,9,3,1]
Output: 12
```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

**Approach**

Scan the amounts from left to right. For each house, take the larger of the previous best total and the current amount plus the best total from two houses back. Track only those two totals for O(n) time and O(1) auxiliary space.
