class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 2
        for _ in range(2, n):
            temp = curr
            curr += prev
            prev = temp
        return n if n == 1 else curr

print(Solution().climbStairs(4))