class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 0
        if n < 3:
            return n
        else:
            a1 = 1
            a2 = 2
            for dummy_idx in range(3, n + 1):
                curr = a1 + a2
                a1 = a2
                a2 = curr
            return curr


sol = Solution()

print(sol.climbStairs(7))
