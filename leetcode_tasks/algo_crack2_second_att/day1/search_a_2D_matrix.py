from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low, row_high = 0, len(matrix) - 1
        while row_low <= row_high:
            row_middle = (row_low + row_high) // 2
            if matrix[row_middle][0] <= target <= matrix[row_middle][-1]:
                row_index = row_middle
                break
            elif matrix[row_middle][0] < target:
                row_low = row_middle + 1
            else:
                row_high = row_middle - 1
        else:
            return False

        col_low, col_high = 0, len(matrix[0]) - 1
        curr_row = matrix[row_index]
        while col_low <= col_high:
            col_middle = (col_low + col_high) // 2
            if curr_row[col_middle] == target:
                return True
            elif curr_row[col_middle] < target:
                col_low = col_middle + 1
            else:
                col_high = col_middle - 1

