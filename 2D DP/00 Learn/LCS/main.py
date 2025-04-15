# Q: Given two strings s1 and s2, find the length of the longest common subsequence between
# the two strings
s1 = "ADCB"
s2 = "ABC"

# Brute Force
def dfs(s1, s2):
    return dfsHelper(s1, s2, 0, 0)

def dfsHelper(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + dfsHelper(s1, s2, i+1, j+1)
    else:
        return max(
            dfsHelper(s1, s2, i+1, j),
            dfsHelper(s1, s2, i, j+1)
        )

print(dfs(s1, s2))

# Memorization approach
def memorization(s1, s2):
    M = len(s1)
    N = len(s2)
    cache = [[-1]*N for _ in range(M)]
    return memorizationHelper(s1, s2, 0, 0, cache)

def memorizationHelper(s1, s2, i, j, cache):

    if i == len(s1) or j == len(s2):
        return 0

    if cache[i][j] != -1:
        return cache[i][j]

    if s1[i] == s2[j]:
        cache[i][j] = 1 + memorizationHelper(s1, s2, i+1, j+1, cache)
    else:
        cache[i][j] = max(
            memorizationHelper(s1, s2, i+1, j, cache),
            memorizationHelper(s1, s2, i, j+1, cache)
        )

    return cache[i][j]

print(memorization(s1, s2))

# Dynamic Programming
def dp(s1, s2):
    M = len(s1)
    N = len(s2)
    dp = [[0]*(N+1) for _ in range(M+1)]

    for i in range(M):
        for j in range(N):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(
                    dp[i][j+1],
                    dp[i+1][j]
                )
    return dp[M][N]

print(dp(s1, s2))
