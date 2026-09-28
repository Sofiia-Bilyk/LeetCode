from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # version 1. Time Limit Exceeded 19 / 24 testcases passed. Checking all the combinations from the start of the array
        '''
        for num1 in numbers:
            if num1 > target:
                return False
            index1 = numbers.index(num1)
            index2 = index1 + 1
            while numbers[index1] + numbers[index2] < target and index2 < len(numbers)-1 :
                index2 += 1
            if numbers[index1] + numbers[index2] == target:
                return [index1+1, index2+1]
        return False
        '''
        # version 2. Checking combinations, having one pointer at the beginning and one pointer at the end of the array
        index1 = 0
        index2 = len(numbers) - 1
        while index1 != index2:
            if numbers[index1] + numbers[index2] < target:
                index1 += 1
            elif numbers[index1] + numbers[index2] > target:
                index2 -= 1
            else:
                return [index1 + 1, index2 + 1]
        return []
