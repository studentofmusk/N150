from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)

        return res





solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))
print(solution.maxProfit([10,8,7,5,2]))
