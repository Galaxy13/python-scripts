from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]

        def find_lists(index, direction):
            try:
                if nums[index] == target and index >= 0:
                    return find_lists(index + direction, direction)
            except IndexError:
                return [index - direction]
            return [index - direction]

        low, high = 0, len(nums)
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                final = find_lists(middle - 1, -1) + find_lists(middle + 1, 1)
                return [final[0], final[-1]]
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return [-1, -1]

if __name__ == '__main__':
    print(Solution().searchRange([3, 3, 3], 3))
