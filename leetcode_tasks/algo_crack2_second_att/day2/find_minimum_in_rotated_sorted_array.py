from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while 1:
            if low >= high:
                return nums[low]
            middle = (low + high) // 2
            if nums[middle] > nums[-1]:
                low = middle + 1
            else:
                high = middle
