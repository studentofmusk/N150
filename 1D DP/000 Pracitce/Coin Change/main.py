class Solution:
    @staticmethod
    def coin_change(coins: list[int], target: int):
        coins.sort()
        dp = [float("inf")] * (target+1)
        dp[0] = 0

        for i in range(1, target+1):
            for coin in coins:
                if coin > i: break

                dp[i] = min(
                    dp[i-coin] + 1,
                    dp[i]
                )

        return dp[target] if dp[target] != float("inf") else -1


print(Solution.coin_change(
    coins = [25, 10, 5, 30], target = 30
))