from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_map = {}
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != ".":
                    #checking row
                    if ("r", i) not in my_map:
                        my_map[("r", i)] = [board[i][j]]
                    else:
                        if board[i][j] not in my_map[("r", i)]:
                            my_map[("r", i)].append(board[i][j])
                        else:
                            return False
                    #checking column
                    if ("c", j) not in my_map:
                        my_map[("c", j)] = [board[i][j]]
                    else:
                        if board[i][j] not in my_map[("c", j)]:
                            my_map[("c", j)].append(board[i][j])
                        else:
                            return False
                    #checking block
                    if ("b", i // 3, j // 3) not in my_map:
                        my_map[("b", i // 3, j // 3)] = [board[i][j]]
                    else:
                        if board[i][j] not in my_map[("b", i // 3, j // 3)]:
                            my_map[("b", i // 3, j // 3)].append(board[i][j])
                        else:
                            return False
        return True
