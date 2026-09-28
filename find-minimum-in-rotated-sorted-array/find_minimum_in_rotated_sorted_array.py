from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid - 1
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            mid = (start + end) // 2
        return nums[mid]
