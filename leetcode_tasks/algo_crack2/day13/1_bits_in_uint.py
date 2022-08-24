class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while -1 + (1 << 32) & n:  # operator & (bit AND) checks, that n is consists at least 1 one-bit,
            # -1 + (1 << 32) is maximum of unsigned 32-bit int (basically all ones)
            c += n & 1  # + 1 to count bits, if last bit is bit-one
            n = n >> 1  # perform right-shifting in n
        return c
