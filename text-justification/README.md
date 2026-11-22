# 68. Text Justification

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/text-justification/description/

Given a list of words and a width `maxWidth`, return lines containing exactly `maxWidth` characters each. Keep the words in their original order and fit as many as possible on each line.

Distribute spaces evenly between words, giving any leftover spaces to the leftmost gaps. For the last line and any line containing a single word, use one space between words and pad the right side to reach `maxWidth`.

**Example 1:**

```
Input: words = ["This","is","an","example","of","text","justification."], maxWidth = 16
Output: ["This    is    an", "example  of text", "justification.  "]
```

**Example 2:**

```
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output: ["What   must   be", "acknowledgment  ", "shall be        "]
```

**Example 3:**

```
Input: words = ["Science","is","what","we","understand","well","enough","to",
                "explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output: ["Science  is  what we", "understand      well", "enough to explain to",
         "a  computer.  Art is", "everything  else  we", "do                  "]
```

**Constraints:**

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `1 <= maxWidth <= 100`
- Each word consists of non-space characters and fits within `maxWidth`.
