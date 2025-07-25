class Solution:
    @staticmethod
    def numOfPaths(n: int, m:int)->int:
        
        dp = [1] * (m+1)
        dp[m] = 0
        
        for _ in range(n-1):
            for i in range(m-1, -1, -1):
                dp[i] = dp[i] + dp[i+1]
        
        return dp[0]

    def memo(self, n:int, m:int)->int:
        cache: dict[tuple[int, int], int] = {}
        def dfs(n:int, m:int)->int:
            if n==1 or m==1:
                return 1
            if (n, m) in cache:
                return cache[(n, m)]

            cache[(n, m)] = dfs(n-1, m) + dfs(n, m-1)

            return cache[(n, m)]

        return dfs(n, m)
    


    def dfs(self, n:int, m:int)->int:
        
        if n==1 or m==1:
            return 1

        return self.dfs(n-1, m) + self.dfs(n, m-1)
    

test_cases = [
    {"n":1, "m":2},
    {"n":3, "m":2},
    {"n":3, "m":3},
]

for test in test_cases:
    print(Solution.numOfPaths(**test)) # O(n * m)
    print(Solution().memo(**test)) # O(n * m)
    print(Solution().dfs(**test)) # O(2^(n + m))
