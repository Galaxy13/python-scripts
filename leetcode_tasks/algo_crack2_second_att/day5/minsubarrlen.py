import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        subset_sum = 0
        min_size = math.inf
        while right < len(nums):
            if nums[right] >= target:
                return 1
            if subset_sum + nums[right] >= target:
                min_size = min(min_size, right - left + 1)
                subset_sum -= nums[left]
                left += 1
            else:
                subset_sum += nums[right]
                right += 1
        return min_size if min_size < math.inf else 0

print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))