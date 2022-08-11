class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        temp_div = 0
        while abs(temp_div + divisor) <= abs(dividend):
            temp_div += divisor
            count += 1
        if divisor ^ dividend < 0:
            return -count
        return count

print(Solution().divide(10000000, -5))
