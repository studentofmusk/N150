class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j >= len(t):
                return 1

            if i >= len(s):
                return 0

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                cache[(i, j)] = dfs(i+1, j)

            return cache[(i, j)]

        return dfs(0, 0)

    def dp(self, s:str, t: str) -> int:
        M = len(s)
        N = len(t)
        dp = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M+1):
            dp[i][N] = 1

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]


print(Solution().numDistinct(s = "caaat", t = "cat"))
print(Solution().numDistinct(s = "xxyxy", t = "xy"))
print(Solution().dp(s = "caaat", t = "cat"))
print(Solution().dp(s = "xxyxy", t = "xy"))

# Count Subsequences
#
# You are given two strings s and t, both consisting of english letters.
#
# Return the number of distinct subsequences of s which are equal to t.
#
# Example 1:
#
# Input: s = "caaat", t = "cat"
#
# Output: 3
#
# Explanation: There are 3 ways you can generate "cat" from s.
#
#     (c)aa(at)
#     (c)a(a)a(t)
#     (ca)aa(t)
#
# Example 2:
#
# Input: s = "xxyxy", t = "xy"
#
# Output: 5
#
# Explanation: There are 5 ways you can generate "xy" from s.
#
#     (x)x(y)xy
#     (x)xyx(y)
#     x(x)(y)xy
#     x(x)yx(y)
#     xxy(x)(y)
#
# Constraints:
#
#     1 <= s.length, t.length <= 1000
#     s and t consist of English letters.
#
