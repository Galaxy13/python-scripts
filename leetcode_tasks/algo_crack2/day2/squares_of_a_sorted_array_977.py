class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pointer1, pointer2 = 0, len(nums) - 1
        square_arr = []
        while pointer1 <= pointer2:
            if nums[pointer1] ** 2 < nums[pointer2] ** 2:
                square_arr.insert(0, nums[pointer2] ** 2)
                pointer2 -= 1
            else:
                square_arr.insert(0, nums[pointer1] ** 2)
                pointer1 += 1
        return square_arr
