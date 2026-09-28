class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(t)
        for letter in s:
            while i < n and t[i] != letter:
                i += 1
            if i == n:
                return False
            i += 1
        return True


'''

        index = 0
        for letter in s:
            if letter in t[index::]: #checking if letter exists AFTER the previously found one
                index = len(t[0:index]) + t[index::].index(letter) + 1 # resetting the index next after just found letter
                if index > len(t):
                    return False
            else:
                return False
        return True
'''
