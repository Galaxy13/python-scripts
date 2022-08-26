class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = [] # list of permutations
        perm_len = len(nums) # len of start array
        def dfs(partitial_nums, perm):
            if len(perm) == perm_len:
                perms.append(perm)    # append your permuation to final array if len of perm is equal to len of start array
            for num_index in range(len(partitial_nums)):
                dfs(partitial_nums[0:num_index] + partitial_nums[num_index + 1:],
                    perm + [partitial_nums[num_index]])    # recursive call of dfs with sliced array (without number, that was appended to permutation) and permutaion with new number
        dfs(nums, [])
        return perms

print(Solution().permute([1]))