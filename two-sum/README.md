# 1. Two Sum

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/two-sum/description/

Given an integer array `nums` and a `target`, return the indices of two elements whose values add up to `target`. Exactly one valid pair exists. The indices must be distinct and may be returned in either order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

**Approach**

Scan the array once, storing the index of each value in a dictionary. Before storing the current value, look up its complement (`target - num`) among earlier values. This guarantees that the two indices are distinct. The algorithm takes O(n) expected time and O(n) space.
