class Solution:
    def coinchange(self, arr: list[int], target: int):
        
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in arr:
            for i in range(num, target+1):
                dp[i]  = dp[i - num] + dp[i]

        return dp[target]

solution = Solution()
print(solution.coinchange(
    arr = [1,2,3],
    target=4
))