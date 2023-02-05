from leetcode_tasks.algo_crack2_second_att.day1.search_a_2D_matrix import Solution as s

def test_algo():
    func = s().searchMatrix
    assert func([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    assert not func([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    assert not func([[1]], 0)