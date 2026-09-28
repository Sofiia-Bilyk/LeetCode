from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        max_side = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                    if matrix[i][j] > max_side:
                        max_side = matrix[i][j]

                elif matrix[i][j] == "0":
                    matrix[i][j] = 0

                else:
                    matrix[i][j] = 1 + min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    )

                    if matrix[i][j] > max_side:
                        max_side = matrix[i][j]


        return max_side**2



        '''
        n = len(matrix)
        m = len(matrix[0])
        size = 0
        new_s = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    new_s = 0
                    end = j + 1
                    while end < m:
                        if matrix[i][end] == "1":
                            end += 1
                        else:
                            break
                    if end == m:
                        end -= 1
                    print(i, j, end)
                    for row in range(i,min(n, end - j + 1)):
                        if "0" in matrix[row][j:end+1] :
                            new_s = 0
                            break
                        else:
                            new_s += 1
                size = max(size, new_s)
        return size**2

        '''
        '''
        m = len(matrix[0])
        n = len(matrix)
        side = 0

        def check_sq(i, j, depth):
            while (i + depth) < n and (j + depth) < m:
                if matrix[i][j+depth] == 1  and matrix[i+depth][j] == 1:
                    for hor in range (j, j + depth + 1):
                        if matrix[i+depth][hor] != "1":
                            return depth
                    for vert in range (i, i + depth + 1):
                        if matrix[vert][j+depth] != "1":
                            return depth
                    depth += 1
                else:
                    return depth
            return depth

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    s = check_sq(i, j, 1)
                    print(s)
                    side = max(side, s)

        return side
        '''
