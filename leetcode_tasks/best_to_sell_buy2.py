class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = prices[0]
        diff_max = 0
        for index in range(len(prices)):
            if min_val > prices[index]:
                min_val = prices[index]
            elif prices[index] - min_val > diff_max:
                diff_max = prices[index] - min_val
        return diff_max

sol = Solution()

arr = [11,2,7,1,4]

print(sol.maxProfit(arr))