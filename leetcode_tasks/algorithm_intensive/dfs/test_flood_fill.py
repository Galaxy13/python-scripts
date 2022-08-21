from flood_fill import Solution

solution = Solution()

def test_flood_fill():

    assert solution.floodFill(image=[[1,1,1], [1,1,0], [1,0,1]], sr=1, sc=1, newColor=3) == [[3,3,3], [3,3,0], [3,0,1]]
    assert solution.floodFill([[1,1,1], [1,1,0], [1,0,1]], sr=0, sc=0, newColor=3) == [[3,3,3], [3,3,0], [3,0,1]]
    assert solution.floodFill([[1]], sr=0, sc=0, newColor=512) == [[512]]
    assert solution.floodFill([[1, 1], [1, 1], [1, 1], [1, 1]], sr=3, sc=0, newColor=35) == [[35, 35], [35, 35],
                                                                                             [35, 35], [35, 35]]