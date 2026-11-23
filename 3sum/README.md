# 15. 3Sum

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/3sum/description/

Given an integer array `nums`, return all unique triplets of values that sum to zero. Each triplet must use three distinct indices. Triplets and their values may be returned in any order.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints:**

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

**Approach**

Sort a copy of the input and fix the first value of each triplet. Scan the remaining range with two pointers. Move the left pointer right when the sum is too small and the right pointer left when it is too large. Skip repeated first values and repeated pointer values after recording a match. The algorithm takes O(n²) time and O(n) auxiliary space, excluding the returned triplets.
