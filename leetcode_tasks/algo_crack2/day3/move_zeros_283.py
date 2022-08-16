class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index1, index2 = 0, len(nums) - 1
        while index1 <= index2:
            if not nums[index1]:
                nums.pop(index1), nums.append(0)
                index2 -= 1
            elif not nums[index2]:
                nums.pop(index2), nums.append(0)
                index1 += 1
            else:
                index1, index2 = index1 + 1, index2 - 1

