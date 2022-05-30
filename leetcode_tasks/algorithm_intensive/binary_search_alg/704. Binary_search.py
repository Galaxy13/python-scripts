class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        middle_index = len(nums) // 2
        if nums[middle_index] == target:
            return middle_index

        if nums[middle_index] < target:
            index = self.search(nums[middle_index + 1:], target)
            if index != -1:
                return index + middle_index + 1
        elif nums[middle_index] > target:
            return self.search(nums[:middle_index], target)

        return -1

print(Solution().search([-1,0,3,5,9,12],2))