from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) in [1, 2]:
            return max(nums)

        def find_max(nums):
            n = len(nums)
            robbed = [0] * n
            robbed[0] = nums[0]
            robbed[1] = nums[1]
            for i in range(2, n):
                robbed[i] = max(robbed[i-1], nums[i] + robbed[i-2])
            return robbed[-1]


        return max(find_max(nums[:-1]), find_max(nums[1:]))
