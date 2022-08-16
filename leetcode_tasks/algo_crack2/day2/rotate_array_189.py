class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = id(nums)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        if start == id(nums): return nums
