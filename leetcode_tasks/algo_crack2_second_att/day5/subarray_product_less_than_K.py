from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = output = 0
        init_k = 1
        for right in range(len(nums)):
            init_k *= nums[right]
            if init_k >= k:
                while init_k >= k and left <= right:
                    init_k //= nums[left]
                    left += 1
            output += right - left + 1
        return output