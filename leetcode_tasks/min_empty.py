from typing import List
class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while i in nums:
            i += 1
        return i

print(Solution.firstMissingPositive([7,8,9,11,12]))