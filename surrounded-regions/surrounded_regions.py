from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board[0])
        n = len(board)

        def dfs(i, j):
            board[i][j] = "C" #mark Checked cells
            if i + 1 < n:
                if board[i+1][j] == "O":
                    dfs(i+1, j)
            if i - 1 >= 0:
                if board[i-1][j] == "O":
                    dfs(i-1, j)
            if j + 1 < m:
                if board[i][j+1] == "O":
                    dfs(i, j+1)
            if j-1 >= 0 :
                if board[i][j-1] == "O":
                    dfs(i, j-1)
        # mark all islands that are not surrounded by
        # checking which ones have at least one cell on the edge
        for k in range(m):
            if board[0][k] == "O":
                dfs(0, k)
            if board[n-1][k] == "O":
                dfs(n-1, k)
        for l in range(n):
            if board[l][0] == "O":
                dfs(l, 0)
            if board[l][m-1] == "O":
                dfs(l, m-1)
        #marking surrounded islands
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "C":
                    board[i][j] = "O"
