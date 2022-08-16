class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        middle_index = len(nums) // 2
        if nums[middle_index] == target:
            return middle_index

        if nums[middle_index] < target:
            index = self.searchInsert(nums[middle_index + 1:], target)
            return index + middle_index + 1
        elif nums[middle_index] > target:
            return self.searchInsert(nums[:middle_index], target)
        return 0
