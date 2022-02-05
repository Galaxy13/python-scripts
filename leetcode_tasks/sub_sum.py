class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for index in range(left, right + 1):
            sum += self.nums[index]
        return sum


nums = NumArray([-2, 0, 3, -5, 2, -1])

print(nums.sumRange(2, 5))