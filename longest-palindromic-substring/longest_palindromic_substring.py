class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = best_end = 0

        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                start, end = left + 1, right
                if end - start > best_end - best_start:
                    best_start, best_end = start, end

        return s[best_start:best_end]
