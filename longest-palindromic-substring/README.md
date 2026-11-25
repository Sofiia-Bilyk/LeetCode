# 5. Longest Palindromic Substring

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string `s`, return a longest contiguous substring that reads the same forward and backward. Any longest match is valid.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
```

`"aba"` is also valid.

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` contains only digits and English letters.

**Approach**

Expand outward from each character for odd-length palindromes and from each gap for even-length palindromes. Track the bounds of the longest match and slice the string once at the end. This takes O(n²) time and O(1) auxiliary space, excluding the returned substring.
