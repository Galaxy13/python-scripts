from leetcode_tasks.algo_crack2_second_att.day1.search_in_rotated_sorted_array import Solution as s

def test_algo():
    func = s().search
    assert func([4,5,6,7,0,1,2], 3) == -1
    assert func([4,5,6,7,0,1,2], 4) == 0
    assert func([4,5,6,7,0,1,2], 2) == 6
    assert func([1,2,3,4,5], 1) == 0
    assert func([1,2,3,4,5], 5) == 4
    assert func([3,4,5,0,1,2], 2) == 5
    assert func([1,2], 1) == 0
    assert func([1], 0) == -1
    assert func([4,5,6,7,0,1,2], 6) == 2
    assert func([5,1,3], 5) == 0
    assert func([1,3], 3) == 1