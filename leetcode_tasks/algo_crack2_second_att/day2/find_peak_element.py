from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while 1:
            middle = (low + high) // 2
            if middle != low or middle != high:
                if nums[middle] < nums[middle + 1]:
                    low = middle + 1
                elif nums[middle - 1] > nums[middle]:
                    high = middle - 1
                elif nums[middle - 1] < nums[middle] > nums[middle + 1]:
                    return middle
            else:
                return middle