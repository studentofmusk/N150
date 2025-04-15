from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i >= len(coins):
                return 0

            if (i, total) in cache:
                return cache[(i, total)]

            res = dfs(i, total+coins[i]) + dfs(i+1, total)

            cache[(i, total)] = res

            return res

        return dfs(0, 0)

    def dp(self, amount: int, coins: List[int]) -> int :
        ## O(n)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            nextDp = [0] * (amount+1)
            nextDp[0] = 1

            for a in range(1, amount+1):
                nextDp[a] = dp[a]
                if a-coins[i] >= 0:
                    nextDp[a] += nextDp[a-coins[i]]
            dp = nextDp

        return dp[amount]

        ## O(m*n) memory complexity
        # dp = [[0] * (len(coins) + 1) for i in range(amount+1)]
        # dp[0] = [1] * (len(coins)+1)
        #
        # for a in range(1, amount+1):
        #     for i in range(len(coins)-1, -1, -1):
        #         dp[a][i] = dp[a][i+1]
        #         if a-coins[i] >= 0:
        #             dp[a][i] += dp[a-coins[i]][i]
        # return dp[amount][0]


print(Solution().change(amount = 4, coins = [1,2,3]))
print(Solution().dp(amount = 4, coins = [1,2,3]))


# Coin Change II
#
# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
#
# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.
#
# You may assume that you have an unlimited number of each coin and that each value in coins is unique.
#
# Example 1:
#
# Input: amount = 4, coins = [1,2,3]
#
# Output: 4
#
# Explanation:
#
#     1+1+1+1 = 4
#     1+1+2 = 4
#     2+2 = 4
#     1+3 = 4
#
# Example 2:
#
# Input: amount = 7, coins = [2,4]
#
# Output: 0
#
# Constraints:
#
#     1 <= coins.length <= 100
#     1 <= coins[i] <= 1000
#     0 <= amount <= 1000
#
