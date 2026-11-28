# 7. Reverse Integer

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/reverse-integer/description/

Reverse the decimal digits of the signed 32-bit integer `x`, preserving its sign. Return `0` if the reversed value falls outside the signed 32-bit range. Use only values that fit in a signed 32-bit integer.

**Example 1:**

```
Input: x = 123
Output: 321
```

**Example 2:**

```
Input: x = -123
Output: -321
```

**Example 3:**

```
Input: x = 120
Output: 21
```

**Constraints:**

- `-2^31 <= x <= 2^31 - 1`

**Approach**

Work with nonpositive values because the signed 32-bit range includes one more negative value than positive values. Use division and remainder by `-10` to remove the last digit. Before appending it, check whether multiplying the current result by ten and adding the digit would exceed the limit for the original sign. This takes O(d) time for d decimal digits and O(1) auxiliary space.
