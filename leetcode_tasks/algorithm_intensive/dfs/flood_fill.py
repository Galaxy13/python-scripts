class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        width, length = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                if x >= 1:
                    dfs(x - 1, y)
                if x < width - 1:
                    dfs(x + 1, y)
                if y >= 1:
                    dfs(x, y - 1)
                if y < length - 1:
                    dfs(x, y + 1)

        dfs(sr, sc)
        return image
