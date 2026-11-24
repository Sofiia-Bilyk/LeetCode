# 238. Product of Array Except Self

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array `nums`, return an array where the value at each index is the product of all input values at other indices. Use O(n) time and avoid division.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- Each prefix product, suffix product, and output value fits in a 32-bit integer.

**Approach**

Scan from left to right to store the product of all values to the left of each index in the output array. Then scan from right to left, multiplying each output entry by the running product of all values to its right. The two passes take O(n) time and O(1) auxiliary space, excluding the output.
