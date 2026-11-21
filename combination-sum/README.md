# 39. Combination Sum

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/combination-sum/description/

Given an array of distinct positive integers `candidates` and an integer `target`, return all unique combinations whose elements sum to `target`. The combinations may appear in any order.

Each candidate may be used any number of times. Two combinations are distinct when they use at least one candidate a different number of times. Each test case has fewer than 150 valid combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All candidates are distinct.
- `1 <= target <= 40`
