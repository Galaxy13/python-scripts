from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[low] <= nums[middle]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1

if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2], 0))
