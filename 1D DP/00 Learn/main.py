# Brute Force
def bruteForce(n):
    if n < 2:
        return n
    return bruteForce(n-1) + bruteForce(n-2)


# Memorization
def memorization(n, cache):
    if n < 2:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memorization(n-1, cache) + memorization(n-2, cache)
    return cache[n]


# Dynamic Programming
def dp(n):
    if n < 2:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i+=1

    return dp[1]


print(bruteForce(6))
print(memorization(6, {}))
print(dp(6))
