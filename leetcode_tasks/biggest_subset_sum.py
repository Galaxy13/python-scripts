class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = best_sum = nums[0]
        for element in nums[1:]:
            max_sum = max(element, max_sum + element)
            best_sum = max(max_sum, best_sum)
        return best_sum

sol = Solution()

print(sol.maxSubArray([5,4,-1,7,8]))