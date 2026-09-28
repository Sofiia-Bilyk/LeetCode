from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        def next_element(i, j, direction):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if j+1 < n and matrix[i][j+1] is not None and direction == "right":
                next_element(i, j+1, direction)
            elif j + 1 >= n or matrix[i][j+1] is None:
                direction = "down"
            if i+1 < m and matrix[i+1][j] is not None and direction == "down":
                next_element(i+1, j, direction)
            elif i + 1 >= m or  matrix[i+1][j] is None:
                direction = "left"
            if j-1 >= 0 and matrix[i][j-1] is not None and direction == "left":
                next_element(i, j-1, direction)
            elif j - 1 < 0 or matrix[i][j-1] is  None:
                direction = "up"
            if i-1 > 0 and matrix[i-1][j] is not None and direction == "up":
                next_element(i-1, j, direction)
            elif i - 1 < 0 or matrix[i-1][j] is not None:
                direction = "right"
            if j+1 < n and matrix[i][j+1] is not None:
                next_element(i, j+1, direction)

        res = []
        if matrix[0][0]:
            next_element(0, 0, "right")

        return res
