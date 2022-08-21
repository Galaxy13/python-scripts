class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pointer1, pointer2 = 0, len(numbers) - 1
        while pointer1 != pointer2:
            if numbers[pointer1] + numbers[pointer2] > target:
                pointer2 -= 1
            elif numbers[pointer1] + numbers[pointer2] < target:
                pointer1 += 1
            else:
                return [pointer1 + 1, pointer2 + 1]
        return -1