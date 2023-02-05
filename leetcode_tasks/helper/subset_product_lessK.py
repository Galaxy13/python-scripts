from leetcode_tasks.algo_crack2_second_att.day5.subarray_product_less_than_K import Solution as s

def test_algo():
    func = s().numSubarrayProductLessThanK
    assert func(nums = [10,5,2,6], k = 100) == 8
    assert func(nums = [1,2,3], k = 0) == 0
    assert func(nums = [4], k=2) == 0
    assert func(nums= [2], k=5) == 1
    assert func(nums=[100, 500], k=1) == 0
    assert func(nums=[1,2], k=10) == 3