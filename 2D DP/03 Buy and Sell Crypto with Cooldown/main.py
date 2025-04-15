from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0

            if (i, isBuy) in cache:
                return cache[(i, isBuy)]

            if isBuy:
                buy = dfs(i+1, False) - prices[i]
                skip = dfs(i+1, True)
                cache[(i, isBuy)] = max(buy, skip)
            else:
                sell = dfs(i+2, True) + prices[i]
                skip = dfs(i+1, False)
                cache[(i, isBuy)] = max(sell, skip)

            return cache[(i, isBuy)]

        return dfs(0, True)

print(Solution().maxProfit(prices = [1,3,4,0,4]))
print(Solution().maxProfit(prices = [1]))


# Buy and Sell Crypto with Cooldown
#
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#
# You may buy and sell one NeetCoin multiple times with the following restrictions:
#
#     After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
#     You may only own at most one NeetCoin at a time.
#
# You may complete as many transactions as you like.
#
# Return the maximum profit you can achieve.
#
# Example 1:
#
# Input: prices = [1,3,4,0,4]
#
# Output: 6
#
# Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.
#
# Example 2:
#
# Input: prices = [1]
#
# Output: 0
#
# Constraints:
#
#     1 <= prices.length <= 5000
#     0 <= prices[i] <= 1000
#
