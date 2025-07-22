class Solution:
    def nth_tribonacci(self, n: int):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp

solution = Solution()

n = 7
print(solution.nth_tribonacci(n))