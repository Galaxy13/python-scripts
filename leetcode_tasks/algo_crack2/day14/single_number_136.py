from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count ^= num
        return count

s = Solution().singleNumber

print(s([4,1,2,1,2]))
