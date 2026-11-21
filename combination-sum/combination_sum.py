from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = [[] for _ in range(target + 1)]
        combinations[0] = [[]]

        for candidate in sorted(candidates):
            # Ascending totals allow the current candidate to be reused.
            for total in range(candidate, target + 1):
                for combination in combinations[total - candidate]:
                    combinations[total].append(combination + [candidate])

        return combinations[target]
