from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_nums = 1
        count_zero = 0
        for item in nums:
            if item:
                product_of_nums *= item
            else:
                count_zero += 1
        if count_zero == 0:
            return [product_of_nums // item for item in nums]
        elif count_zero == 1:
            return [0 if item else product_of_nums for item in nums]
        else:
            return [0] * len(nums)



print(Solution().productExceptSelf([-1,1,0,-3,3]))
