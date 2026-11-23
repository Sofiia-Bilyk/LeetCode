# 49. Group Anagrams

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/group-anagrams/description/

Group the strings in `strs` by anagram. Strings are anagrams when they contain the same letters with the same counts. The groups may be returned in any order.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- Each string consists of lowercase English letters.

**Approach**

Sort each string's letters to create a dictionary key shared by all of its anagrams. Append the original string to the list for that key, then return the dictionary's lists.
