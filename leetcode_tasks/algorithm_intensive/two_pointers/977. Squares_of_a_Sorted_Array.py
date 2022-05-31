class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pointer1 = 0
        pointer2 = len(nums) - 1
        square_nums = []
        while pointer1 <= pointer2:
            if nums[pointer1] ** 2 < nums[pointer2] ** 2:
                square_nums.insert(0, nums[pointer2] ** 2)
                pointer2 -= 1
            else:
                square_nums.insert(0, nums[pointer1] ** 2)
                pointer1 += 1
        return square_nums

print(Solution().sortedSquares([-10,-1,0,3,10]))