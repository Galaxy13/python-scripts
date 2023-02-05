from leetcode_tasks.algo_crack2_second_att.day2.find_peak_element import Solution as s

def test_algo():
    func = s().findPeakElement
    assert func([1,2,3,1]) == 2
    assert func([1,2,1,3,5,6,4]) == 5
    assert func([3,2,1]) == 0
    assert func([1]) == 0
    assert func([1,2,3]) == 2
    assert func([1,2,1,2,1,2]) == 5
