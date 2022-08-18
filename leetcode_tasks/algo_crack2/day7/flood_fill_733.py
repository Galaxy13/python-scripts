class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        newColor = color
        color = image[sr][sc]

        def dfs(sr: int, sc: int):
            try:
                if image[sr][sc] == color and sr >= 0 and sc >= 0 and image[sr][sc] != newColor:
                    image[sr][sc] = newColor
                    dfs(sr - 1, sc)
                    dfs(sr, sc - 1)
                    dfs(sr + 1, sc)
                    dfs(sr, sc + 1)
            except IndexError:
                return

        dfs(sr, sc)
        return image
