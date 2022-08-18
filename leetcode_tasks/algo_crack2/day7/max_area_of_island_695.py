class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        def dfs_island(x, y):
            try:
                if not grid[x][y] or x < 0 or y < 0:
                    return 0
                else:
                    grid[x][y] = 0
                    return (1 +
                            dfs_island(x - 1, y) +
                            dfs_island(x, y - 1) +
                            dfs_island(x + 1, y) +
                            dfs_island(x, y + 1))
            except IndexError:
                return 0

        for width in range(len(grid)):
            for height in range(len(grid[0])):
                if grid[width][height]:
                    area = dfs_island(width, height)
                    max_area = max(area, max_area)
        return max_area
