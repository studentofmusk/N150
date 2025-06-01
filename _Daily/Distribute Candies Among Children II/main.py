from math import comb
class Solution:
    
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for k in range(0, 4):  # 0 to 3 because 3 children
            sign = (-1) ** k
            val = n - k * (limit + 1)
            if val < 0:
                continue
            result += sign * comb(3, k) * comb(val + 2, 2)
        return result
    
    # memory limit exceeded
    def distributeCandies1(self, n: int, limit: int) -> int:
        dp = [[[0]*(n+1) for _ in range(limit+1)] for _ in range(4)]
        dp[0][0][0] = 1

        for child in range(1, 4):
            for prev_candy in range(n+1):
                for take in range(min(limit, n-prev_candy)+1):
                    dp[child][take][prev_candy+take] += sum(dp[child-1][t][prev_candy]  for t in range(limit+1))

        return sum(dp[3][i][n] for i in range(limit+1))  

    # exceed iteration limit (recursive)
    def distributeCandies2(self, n: int, limit: int) -> int:
        cache = {}
        def dfs(candies, limit, children):
            if children == 0:
                if candies == 0:
                    return 1
                else:
                    return 0
            if (candies, children) in cache:
                return cache[(candies, children)]
            ways = 0
            for take in range(min(candies, limit)+1):
                ways += dfs(candies-take, limit, children-1)
            cache[(candies, children)] = ways
            return ways
        
        return dfs(n, limit, 3)      

print(Solution().distributeCandies(
    3, 3
))

