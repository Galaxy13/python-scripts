# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    bad_version = 1
    if version < bad_version:
        return False
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        middle_n = n // 2
        prev_middle_n = n
        while True:
            if not isBadVersion(middle_n):
                middle_n = (prev_middle_n + middle_n) // 2 + ((prev_middle_n + middle_n) % 2)
            else:
                if not isBadVersion(middle_n - 1):
                    return middle_n
                else:
                    prev_middle_n = middle_n
                    middle_n //= 2
