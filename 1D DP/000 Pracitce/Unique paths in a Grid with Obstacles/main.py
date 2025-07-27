class Solution:
    @staticmethod
    def uniquePath(grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * (m+1) for _ in range(n)]
        dp[n-1][m-1] = 1

        # Fill the last row
        for i in range(m-2, -1, -1):
            if grid[n-1][i] != 1:
                dp[n-1][i] = dp[n-1][i+1]
        
        # Fill the last column
        for i in range(n-2, -1, -1):
            if grid[i][m-1] != 1:
                dp[i][m-1] = dp[i+1][m-1]
            
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
    
    @staticmethod
    def uniquePathRecru(grid: list[list[int]])->int:
        n, m = len(grid), len(grid[0])

        if grid[0][0] ==1 or grid[n-1][m-1] == 1: return 0

        cache: dict[tuple[int, int], int] = {
            (n-1, m-1): 1
        }

        def dfs(r: int, c: int):

            if (r, c) in cache:
                return cache[(r, c)]
            
            if (
                r >= n or 
                c >= m or 
                grid[r][c] ==1
            ):
                return 0
            

            neighbors = [[0, 1], [1, 0]]
            cache[(r, c)] = 0
            for dr, dc in neighbors:
                cache[(r, c)] += dfs(r+dr, c+dc)
            
            return cache[(r, c)]

        return dfs(0, 0)


test_cases = [
    {
        "grid":[[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
    },
    {
        "grid":[[0, 1],
                [0, 0]]
    },

]

for test in test_cases:
    print(Solution.uniquePath(**test)) # O(n * m)
    print(Solution.uniquePathRecru(**test)) # O(n * m)