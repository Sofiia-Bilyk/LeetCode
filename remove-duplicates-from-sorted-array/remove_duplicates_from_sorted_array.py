from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        res = list(set(nums))
        res.sort()
        k = len(res)
        for i in range(k):
            nums[i] = res[i]
        for i in range(k, n):
            nums[i] = "_"
        return k
