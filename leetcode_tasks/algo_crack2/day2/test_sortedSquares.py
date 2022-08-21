from squares_of_a_sorted_array_977 import Solution as s

sol = s().sortedSquares

def test_sortedSquares():
    assert sol([-1]) == [1]
    assert sol([3]) == [9]
    assert sol([-1, 1]) == [1, 1]
    assert sol([-4, 0, 3]) == [0, 9, 16]