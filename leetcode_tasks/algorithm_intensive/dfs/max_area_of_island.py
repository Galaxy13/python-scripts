class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited_grid = [[0 for dummy_w in range(len(grid[0]))] for dummy_l in range(len(grid))]
        length, width = len(grid), len(grid[0])
        island_max = set()
        def dfs_of_grid(grid_y, grid_x):
            if not (0 <= grid_y < length and 0 <= grid_x < width and not visited_grid[grid_y][grid_x] and grid[grid_y][grid_x]):
                return 0
            visited_grid[grid_y][grid_x] = 1
            return (1 + dfs_of_grid(grid_y + 1, grid_x) + dfs_of_grid(grid_y - 1, grid_x) + dfs_of_grid(grid_y, grid_x + 1)
                    + dfs_of_grid(grid_y, grid_x - 1))

        for x in range(width):
            for y in range(length):
                island_max.add(dfs_of_grid(y, x))
        return max(island_max)

print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0]]))
