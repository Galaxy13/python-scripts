from two_sumii_167 import Solution as s

twoSum = s().twoSum

def test_twoSum():
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 7, 11, 18], 29) == [3, 4]
    assert twoSum([2, 3, 4], 9) == -1
    assert twoSum([0, 0], 1) == -1
    assert twoSum([0, 1], 1) == [1, 2]