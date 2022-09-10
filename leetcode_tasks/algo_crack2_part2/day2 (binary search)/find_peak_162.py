from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return nums.index(max(nums))
        low, high = 0, len(nums) - 1
        while low < high + 1:
            middle = (low + high) // 2
            if middle == 0 or middle == high:
                return middle
            if 0 < middle < len(nums):
                if nums[middle] > nums[middle - 1] and nums[middle] > nums[middle + 1]:
                    return middle
                else:
                    if nums[middle] < nums[middle - 1]:
                        high = middle
                    else:
                        low = middle + 1


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
