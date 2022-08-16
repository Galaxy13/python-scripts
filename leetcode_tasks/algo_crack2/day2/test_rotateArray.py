from rotate_array_189 import Solution as s

sol = s().rotate


def test_rotateArray():
    assert sol([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert sol([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert sol([1, 2, 3, 4, 5, 6, 7], 10) == [5, 6, 7, 1, 2, 3, 4]
