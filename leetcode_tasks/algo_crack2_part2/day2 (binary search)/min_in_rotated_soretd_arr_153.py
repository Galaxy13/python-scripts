from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        min = float('inf')
        while low <= high:
            middle = (low + high) // 2
            if nums[0] < nums[middle]:
                if nums[0] < min and nums[0] < nums[middle]:
                    min = nums[0]
                low = middle + 1
            else:
                if nums[middle] <= nums[high]:
                    high = middle - 1
                else:
                    low = middle + 1
                if min > nums[middle]:
                    min = nums[middle]
        return min


if __name__ == '__main__':
    print(Solution().findMin([1,2,3]))
