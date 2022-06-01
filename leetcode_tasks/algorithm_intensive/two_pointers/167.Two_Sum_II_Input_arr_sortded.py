class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1, index2 = 0, len(numbers) - 1
        while index1 != index2:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                return [index1 + 1, index2 + 1]

print(Solution().twoSum([0, 1], 2))