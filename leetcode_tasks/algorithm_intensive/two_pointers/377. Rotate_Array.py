class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 1 or not k: return
        if k > n: k = k % n
        nums[:] = nums[-k:] + nums[:len(nums) - k]
        print(nums)


Solution().rotate([1, 2], 2)
