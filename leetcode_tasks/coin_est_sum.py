class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins = sorted(coins)
        if not amount:
            return 0
        coin_idx = -1
        count = 0
        while coin_idx >= -(len(coins)):
            if coins[coin_idx] > amount:
                coin_idx -= 1
                continue
            # initial_amount = int(amount)
            count += amount // coins[coin_idx]
            if amount % coins[coin_idx] == 0:
                return count
            else:
                count_temp = self.coinChange(coins[:coin_idx], amount % coins[coin_idx])
                if count_temp == -1:
                    count = 0
                    coin_idx -= 1
                else:
                    return count_temp + count
        return -1


sol = Solution()
print(sol.coinChange([186,419,83,408], 6249))

