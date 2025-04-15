from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0]*(n+2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    coins = new_nums[l-1] * new_nums[i] * new_nums[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]





    def TopBottum(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums)-2)

    def BruteForce(self, nums: List[int]) -> int:
        # Pad nums with 1 at the start and end to handle edge cases easily
        nums = [1] + nums + [1]

        def dfs(nums):
            if len(nums) == 2:
                return 0
            max_coins = 0

            for i in range(1, len(nums)-1):
                coins = nums[i-1] * nums[i] * nums[i+1]
                coins += dfs(nums[:i]+nums[i+1:])
                max_coins = max(max_coins, coins)
            return max_coins
        return dfs(nums)


print(Solution().maxCoins( [4,2,3,7]))
print(Solution().TopBottum( [4,2,3,7]))



# Burst Balloons
#
# You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.
#
# If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bound value is 1.
#
# Return the maximum number of coins you can receive by bursting all the balloons.
#
# Example 1:
#
# Input: nums = [4,2,3,7]
#
# Output: 143
#
# Explanation:
# nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
# coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143
#
# Constraints:
#
#     n == nums.length
#     1 <= n <= 300
#     0 <= nums[i] <= 100
#
