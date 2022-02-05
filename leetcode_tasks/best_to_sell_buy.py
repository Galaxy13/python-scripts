class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dummy_var = 0
        while dummy_var < len(prices) // 2:
            min_price_a = prices.index(min(prices))
            max_price_a = prices.index(max(prices))
            if prices[min_price_a] is prices[-1]:
                prices = prices[:-1]
                continue
            elif prices[max_price_a] is prices[0]:
                prices = prices[1:]
            else:
                max_price_b = prices.index(max(prices[min_price_a:]))
                min_price_b = prices.index(min(prices[:max_price_a]))
                price_a = prices[max_price_b] - prices[min_price_a]
                price_b = prices[max_price_a] - prices[min_price_b]
                return (price_a if price_a > price_b else price_b)
        return 0


sol = Solution()

