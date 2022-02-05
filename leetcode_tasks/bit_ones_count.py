class Solution:
    def countBits(self, n: int) -> list[int]:
        return [bin(num).count('1') for num in range(0, n + 1)]


sol = Solution()

print(sol.countBits(8))

