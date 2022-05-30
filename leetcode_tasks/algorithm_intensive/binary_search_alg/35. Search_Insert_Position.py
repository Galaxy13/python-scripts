class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if len(nums) == 1 and nums[0] > target:
            return -1
        elif len(nums) == 1 and nums[0] < target:
            return 1
        middle_index = len(nums) // 2
        if nums[middle_index] == target:
            return middle_index

        if nums[middle_index] < target:
            return middle_index + self.searchInsert(nums[middle_index:], target)
        else:
            return self.searchInsert(nums[:middle_index], target)

print(Solution().searchInsert([1, 3, 5, 6], 0))