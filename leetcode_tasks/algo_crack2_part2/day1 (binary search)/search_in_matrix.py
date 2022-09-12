from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(nums: List[int]):
            low, high = 0, len(nums) - 1
            while low <= high:
                middle = (low + high) // 2
                if nums[middle] == target:
                    return True
                elif nums[middle] > target:
                    high = middle - 1
                else:
                    low = middle + 1
            return False

        low, high = 0, len(matrix) - 1
        while low <= high:
            middle = (low + high) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                return binarySearch(matrix[middle])
            elif matrix[middle][0] > target:
                high = middle - 1
            else:
                low = middle + 1
        return False


if __name__ == "__main__":
    print(Solution().searchMatrix(matrix=[[1]], target=1))
