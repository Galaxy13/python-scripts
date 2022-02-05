class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        middle_idx = len(nums) // 2
        if nums[middle_idx] == target:
            return middle_idx
        if nums[middle_idx] < target:
            idx_bigger = self.search(nums[middle_idx:], target)
            if idx_bigger != -1:
                return middle_idx + idx_bigger
        else:
            return self.search(nums[:middle_idx], target)
        return -1
