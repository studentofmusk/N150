class Solution:
    @staticmethod
    def cutRod(prices: list[int])->int:
        n = len(prices)
        dp = [0] * (n+1)

        for i in range(1, n+1):
            price = prices[i-1]
            for j in range(i, n+1):
                dp[j] = max(
                    dp[j],
                    dp[j-i] + price
                )
        # print(dp)
        return max(dp)


print(Solution.cutRod(
    prices=[1, 5, 8, 9, 10, 17, 17, 20]
))