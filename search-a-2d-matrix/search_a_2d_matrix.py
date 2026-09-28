from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        row = end // 2

        while start <= end:
            if target < matrix[row][0]:
                end  = row - 1
                row = (start + end) // 2
            elif target > matrix[row][0]:
                start = row + 1
                row = (start + end) // 2
            else:
                return True

        print(matrix[row])
        start = 0
        end = len(matrix[row]) - 1
        j = end // 2

        while start <= end:
            if target < matrix[row][j]:
                end = j-1
                j = (start + end) // 2
            elif  target > matrix[row][j]:
                start = j+1
                j = (start + end) // 2
            else:
                return True
        return False
