from flood_fill_733 import Solution as s

sol = s().floodFill

def test_flood_fill():
    assert sol([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert sol([[0,0,0], [0,0,0]], 0, 0, 0) == [[0,0,0], [0,0,0]]