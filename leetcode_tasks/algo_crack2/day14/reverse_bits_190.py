class Solution:
    def reverseBits(self, n: int) -> int:
        temp = 0 << 32
        for _ in range(32):
            temp <<= 1
            temp |= n & 1
            n >>= 1
        return temp

s = Solution().reverseBits

print(s(0b0000000000000000000000000000000000010010))

