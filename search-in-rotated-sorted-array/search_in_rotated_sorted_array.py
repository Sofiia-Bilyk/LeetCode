from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while start < end:
            if nums[mid] > target:
                if target >= nums [0] or nums[mid] < nums[0]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < target:
                if target >= nums [0] and nums[mid] < nums[0]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] == target:
                    return mid
                else:
                    return -1
            mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        return -1
