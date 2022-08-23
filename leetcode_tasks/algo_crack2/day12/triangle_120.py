from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = []
        num_of_rows = len(triangle)
        for col in triangle[len(triangle) - 1]:
            memo.append(col)

        for row_dp in range(num_of_rows - 2, -1, -1):
            for col_dp in range(row_dp + 1):
                memo[col_dp] = min(memo[col_dp], memo[col_dp + 1]) + triangle[row_dp][col_dp]
        return memo[0]

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))