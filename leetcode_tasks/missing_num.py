class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()


sol = Solution()
print (sol.missingNumber([0, 1, 2, 3, 4]))


# print(set(range(3)))