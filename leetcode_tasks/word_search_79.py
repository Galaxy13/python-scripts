from copy import copy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_valid(irow, icol):
            return 0 <= icol < len(board[0]) and 0 <= irow < len(board) and board[irow][icol]

        def dfs(irow, icol, word):
            if len(word) == 1:
                return True
            temp = board[irow][icol]
            board[irow][icol] = 0
            for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if is_valid(next_row := irow + direction[0], next_col := icol + direction[1]) and \
                        word[1] == board[next_row][next_col]:
                    if dfs(next_row, next_col, word[1:]):
                        return True
            board[irow][icol] = temp

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, word):
                        return True


        return False


print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
                       word="ABCESEEEFS"))
