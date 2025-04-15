# ========================================= 0/1 knapsack =============================================
# Q: Given a list of N items, and backpack with a limited capacity, return the maximum total profit that can be contained
#    in the backpack. The i-th item's profit is profit[i] and it's weight is weight[i]. Assume you can only add each item
#    to the bag at most one time.

profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8
# Output: 12

# Brute Force Solution
# Time: O(2^n), Space: O(n)
# where n is number of items
def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    maxProfit = dfsHelper(i+1, profit, weight, capacity)

    newCap = capacity - weight[i]
    if newCap >=0:
        p = profit[i] + dfsHelper(i+1, profit, weight, newCap)
        # compute the max
        maxProfit = max(maxProfit, p)
    return maxProfit

print(dfs(profit, weight, capacity))

# ----------------------------------------------------------------------------------

# Memorization Solution
# Time: O(m * n), Space: O(m * n)
# where n is number of items & m is capacity
def memorization(profit, weight, capacity):
    N, M = len(profit), capacity
    cache = [[-1] * (M+1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]

    cache[i][capacity] = memoHelper(i+1, profit, weight, capacity, cache)

    newCap = capacity - weight[i]
    if newCap >=0:
        p = profit[i] + memoHelper(i+1, profit, weight, newCap, cache)
        cache[i][capacity] = max(cache[i][capacity], p)

    return cache[i][capacity]

print(memorization(profit, weight, capacity))

# ----------------------------------------------------------------------------------

# Dynamic Programming
# Time: O(n*m), Space: O(n*m)
# where n is number of items and m in capacity
def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0]*(M+1) for _ in range(N)]

    for i in range(N):
        dp[i][0] = 0

    for c in range(M+1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M+1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i-1][c-weight[i]]
            dp[i][c] = max(skip, include)
    return dp[N-1][M]

print(dp(profit, weight, capacity))


# ========================================= unbound knapsack =============================================
# Q:Given a list of N items, and a backpack with a
# # limited capacity, return the maximum total profit that
# # can be contained in the backpack. The i-th item's profit
# # is profit[i] and it's weight is weight[i]. Assume you can
# # have an unlimited number of each item available.

# Brute force Solution
# Time: O(2^m), Space: O(m)
# Where m is the capacity.

def dfs_u(profit, weight, capacity):
    return dfsHelper_u(0, profit, weight, capacity)

def dfsHelper_u(i, profit, weight, capacity):
    if i == len(profit):
        return 0
    maxProfit = dfsHelper_u(i+1, profit, weight, capacity)

    new_cap = capacity - weight[i]

    if new_cap >=0:
        p = profit[i] + dfsHelper_u(i, profit, weight, new_cap)
        maxProfit = max(p, maxProfit)

    return maxProfit

# ----------------------------------------------------------------------------------


# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.

def memorization_u(profit, weight, capacity):
    M, N = len(profit), capacity
    cache = [[-1]*(N+1) for _ in range(M)]
    return memorizationHelper_u(0, profit, weight, capacity, cache)

def memorizationHelper_u(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0

    if cache[i][capacity] != -1:
        return cache[i][capacity]

    cache[i][capacity] = memorizationHelper_u(i+1, profit, weight, capacity, cache)

    new_cap = capacity - weight[i]
    if new_cap >= 0:
        p = profit[i] + memorizationHelper_u(i, profit, weight, new_cap, cache)
        cache[i][capacity] = max(p, cache[i][capacity])

    return cache[i][capacity]

# ----------------------------------------------------------------------------------

def dp_u(profit, weight, capacity):
    M, N = len(profit), capacity
    dp = [[0]*(N+1) for _ in range(M)]

    # can skip
    # for i in range(M):
    #     dp[i][0] = 0

    for c in range(N+1):
        if weight[0] >= c:
            dp[0][c] = profit[0] * (c//weight[0])

    for i in range(1, M):
        for c in range(1, N+1):
            skip = dp[i-1][c]
            include = 0

            if weight[i] <= c:
                include = profit[i] + dp[i][c-weight[i]]
            dp[i][c] = max(skip, include)

    return dp[M-1][N]


# Outputs:

print(dfs_u(profit, weight, capacity))
print(memorization_u(profit, weight, capacity))
print(dp_u(profit, weight, capacity))



