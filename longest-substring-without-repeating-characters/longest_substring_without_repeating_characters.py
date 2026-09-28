class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index1, index2 = 0, 0
        n = len(s)
        if n==0:
            return 0
        max_len = 1
        indeces = {} #traking of the indeces of characters in the slicing window
        indeces[s[0]] = 0
        while index2 + 1 < n:
            index2 += 1
            current = s[index2]
            if current not in indeces:
                indeces[current] = index2
            else:
                index1 = indeces[current] + 1
                indeces[current] = index2
                # deleting all key:value pairs from the dictionary that has index less than a new index1
                indeces = {k: v for k, v in indeces.items() if v >= index1}
            max_len = max(max_len, index2-index1+1)

        return max_len


# O(n^2) -> O(n)
