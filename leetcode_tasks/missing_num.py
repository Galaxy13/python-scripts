class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return set(range(max(nums) + 1)) - set(nums)


sol = Solution()

# print (sol.missingNumber([1, 2, 3, 4]))


print(set(range(3)))