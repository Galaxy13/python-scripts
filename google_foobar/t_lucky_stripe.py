import random
import time

from lucky_stripe import solution

# def test_should_return_number_of_lucky_stripes():
#     # assert solution([1,2,3,4,5,6]) == 3
#     # assert solution([]) == 0
#     # assert solution([1,2,4]) == 1
#     # assert solution([1,1,1]) == 1
#     # assert solution([2, 4, 8, 16, 32]) == 10
#     # assert solution([11,13,17,23, 24, 48, 96]) == 1
#     # assert solution([3, 9, 27]) == 1
#     # assert solution([1, 1]) == 0
#     # assert solution([3, 7, 14, 15, 28]) == 1
#     # assert solution([1, 1, 1, 1]) == 2
#     start = time.time()
#     assert solution([random.randint(1, 1000) for dummy_index in range(2000)])
#     print(time.time() - start)

list_num = [random.randint(1, 1000) for dummy_index in range(20000)]
start = time.time()
solution(list_num)
print(time.time() - start)