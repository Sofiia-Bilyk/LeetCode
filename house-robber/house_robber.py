from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        best_two_back = 0
        best_previous = 0

        for amount in nums:
            best_current = max(best_previous, best_two_back + amount)
            best_two_back = best_previous
            best_previous = best_current

        return best_previous
