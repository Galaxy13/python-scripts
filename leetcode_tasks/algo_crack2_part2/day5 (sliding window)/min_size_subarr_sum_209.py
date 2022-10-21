import sys
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum = 0
        min_size = 2e32
        while right < len(nums):
            if nums[right] >= target:
                return 1
            if sum + nums[right] >= target:
                min_size = min(min_size, right - left + 1)
                sum -= nums[left]
                left += 1
            else:
                sum += nums[right]
                right += 1
        return min_size if min_size < 2e32 else 0

if __name__ == '__main__':
    print(Solution().minSubArrayLen(nums=[2,3,1,2,4,3], target=7))