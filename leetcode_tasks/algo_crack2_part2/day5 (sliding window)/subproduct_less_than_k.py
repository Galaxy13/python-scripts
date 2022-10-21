from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        sliding_product = 1
        count_subarray_count = 0
        while right < len(nums):
            if nums[right] < k:
                if sliding_product * nums[right] < k:
                    count_subarray_count += (right - left + 1)
                    sliding_product *= nums[right]
                    right += 1
                else:
                    sliding_product //= nums[left]
                    left += 1
            else:
                right += 1
                left = right
                sliding_product = 1
        return count_subarray_count


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([100,2,3,4,100,5,6,7,100], 100))
