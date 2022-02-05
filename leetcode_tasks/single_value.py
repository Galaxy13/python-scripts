class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        r = 0
        return [r:=r^n for n in nums][-1]

sol = Solution()

print(sol.singleNumber([1, 2, 3, 1, 2]))

# print([1, 2, 2, 3][0:])

# print(7 ^ 7)
