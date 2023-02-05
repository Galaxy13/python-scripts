from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if target < nums[0]:
                if target < nums[middle] <= nums[-1]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[0] <= nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1
        return -1