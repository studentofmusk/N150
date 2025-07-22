from typing import List

class Solution:
    @staticmethod
    def mincost(cost:List[List[int]]):
        n = len(cost)
        m = len(cost[0])

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = cost[0][0]
        
        # change row: all col: 0
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + cost[i][0]
        
        # change row: 0 col: all
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + cost[0][i]

        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = cost[r][c] + min(
                    dp[r-1][c], 
                    dp[r-1][c-1],
                    dp[r][c-1]
                )
        return  dp[n-1][m-1]      


print(Solution.mincost(
    cost = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]
))