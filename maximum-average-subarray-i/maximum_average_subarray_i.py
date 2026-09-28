from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        index1 = 0
        index2 = k-1
        max_avg = sum(nums[index1:index2+1]) / k
        current_sum =  sum(nums[index1:index2+1])

        while index2 < n:
            if index1 != 0:
                current_sum = current_sum + nums[index2] - nums[index1-1] # re calculating the sum in the sliding window based on the elements that has changed
                max_avg =  max(max_avg, (current_sum) / k)
            index1 += 1
            index2 += 1

        return max_avg
