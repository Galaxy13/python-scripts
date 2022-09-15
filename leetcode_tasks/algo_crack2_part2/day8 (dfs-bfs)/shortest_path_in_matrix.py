from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1)]

        def isValid(new_pos):
            return 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid) and grid[new_pos[0]][new_pos[1]] != 1

        if grid[0][0] or grid[len(grid) - 1][len(grid) - 1]:
            return -1
        queue = [(len(grid) - 1, len(grid) - 1)]
        while queue:
            node = queue.pop(0)
            if node == (0,0):
                return grid[0][0] + 1
            for row, col in DIRECTIONS:
                if isValid(new_node := (node[0] + row, node[1] + col)):
                    if grid[new_node[0]][new_node[1]]:
                        grid[new_node[0]][new_node[1]] = min(grid[node[0]][node[1]] + 1, grid[new_node[0]][new_node[1]])
                    else:
                        grid[new_node[0]][new_node[1]] = grid[node[0]][node[1]] + 1
                    if new_node not in queue:
                        queue.append(new_node)
            grid[node[0]][node[1]] = 1
        return -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))
