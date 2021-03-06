class Solution:
    # def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    #     if len(nums) > len(set(nums)):
    #         return list(set(range(1, len(nums) + 1)) - set(nums))
    #     else:
    #         return list(set(range(1, max(nums) + 1)) - set(nums))

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


sol = Solution()

print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

print(set(range(1, len([1, 2, 3]) + 1)))