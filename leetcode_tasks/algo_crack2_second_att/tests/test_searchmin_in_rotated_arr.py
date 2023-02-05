from leetcode_tasks.algo_crack2_second_att.day2.find_minimum_in_rotated_sorted_array import Solution as s

def test_algo():
    func = s().findMin
    assert func([3,4,5,1,2]) == 1
    assert func([4,5,6,7,0,1,2]) == 0
    assert func([1,2,3,4,5]) == 1
    assert func([1]) == 1
    assert func([2,3,4,5,1]) == 1
    assert func([3,1,2]) == 1