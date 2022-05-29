class Solution:
    def containsDuplicate(self, nums) -> bool:
        temp_dict = {}
        for number in nums:
            try:
                temp_dict[number] += 1
                return True
            except:
                temp_dict[number] = 0
        return False


print(Solution.containsDuplicate([1, 2, 3, 4]))
