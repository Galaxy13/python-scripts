from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        sliding_product = 1
        count_subarray_count = 0
        changed = False
        while right < len(nums) and left < len(nums) - 1:
            if nums[right] < k:
                if sliding_product * nums[right] < k:
                    sliding_product *= nums[right]
                    count_subarray_count += 1
                    if changed:
                        count_subarray_count += 1
                    if right == len(nums) - 1:
                        sliding_product // nums[left] * nums[right]
                        left += 1
                        changed = False
                    else:
                        changed = True
                        right += 1
                else:
                    if changed:
                        count_subarray_count += 1
                    sliding_product //= nums[left]
                    left += 1
                    changed = False
            else:

                right += 1
                left = right
        return count_subarray_count

if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))
