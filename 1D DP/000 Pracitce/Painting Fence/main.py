from functools import lru_cache

class Solution:
    @staticmethod
    def countWays(n: int, k: int) -> int: # n: n of posts | k: n of colors | minimum 2 consequent post can have same color
        
        dp = [0] * (n+1)
        dp[1] = k # diff posts
        dp[2] = k * k # same posts

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        
        return dp[n]

    @staticmethod
    def memo(n:int, k: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(n, k):
            if n ==1:
                return k
            if n == 2:
                return k * k
            
            count1 = dfs(n-1, k) * (k-1)
            count2 = dfs(n-2, k) * (k-1)

            return count1 + count2
        
        return dfs(n, k)

print(Solution.countWays(2, 4))
print(Solution.memo(2, 4))
