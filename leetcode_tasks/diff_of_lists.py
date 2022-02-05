class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        return [num for num in nums if nums.count(num) > 1][0]


sol = Solution()

print(sol.findDuplicate([1, 1, 3]))