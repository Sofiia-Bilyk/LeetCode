class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        index = -1
        l = 0
        while s[index] == ' ':
            index -= 1
            if index *  (-1) > len(s):
                return l

        while s[index] != ' ':
            index -= 1
            l += 1
            if index *  (-1) > len(s):
                return l

        return l
