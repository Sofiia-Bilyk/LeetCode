from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arrangement = nums.copy()
        result = []

        def backtrack(position: int) -> None:
            if position == len(arrangement):
                result.append(arrangement.copy())
                return

            for index in range(position, len(arrangement)):
                arrangement[position], arrangement[index] = arrangement[index], arrangement[position]
                backtrack(position + 1)
                arrangement[position], arrangement[index] = arrangement[index], arrangement[position]

        backtrack(0)
        return result
