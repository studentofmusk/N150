from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)-1):
            Max = max(prices[i+1:])
            if prices[i] < Max:
                best_profit = max(Max-prices[i], best_profit)
            else: continue
        
        return best_profit




solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))
print(solution.maxProfit([10,8,7,5,2]))


# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6

# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0

# Explanation: No profitable transactions can be made, thus the max profit is 0.

