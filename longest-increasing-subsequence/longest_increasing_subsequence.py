from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    count[i] = max(count[i], count[j] + 1)
        return max(count)
