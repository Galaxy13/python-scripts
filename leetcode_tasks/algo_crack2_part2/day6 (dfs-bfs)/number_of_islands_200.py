from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0 and grid[row][col] != 0

        def bfs(irow, icol):
            queue = [(irow, icol)]
            while queue:
                pos = queue.pop(0)
                if grid[pos[0]][pos[1]] == '1':
                    grid[pos[0]][pos[1]] = '2'
                    for x, y in (-1, 0), (1, 0), (0, -1), (0, 1):
                        if isValid(pos[0] + x, pos[1] + y):
                            queue.append((pos[0] + x, pos[1] + y))

        count_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count_of_islands += 1
                    bfs(row, col)
        return count_of_islands

if __name__ == '__main__':
    print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
