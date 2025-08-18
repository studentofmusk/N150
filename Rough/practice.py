from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(price-lowest, profit)
        return profit


solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))
print(solution.maxProfit([10,8,7,5,2]))

