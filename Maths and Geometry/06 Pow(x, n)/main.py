class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        isNegative = n < 0
        if isNegative:
            n = -n

        visit = {}
        def dfs(n):
            if n in visit:
                return visit[n]
            if n == 1:
                return x
            
            if n % 2 == 0:
                visit[n] = dfs(n/2) * dfs(n/2)
            else:
                visit[n] = dfs(n//2) * dfs(n//2) * dfs(1)
            
            return visit[n]
        
        return 1/dfs(n) if isNegative else dfs(n) 

    def myPow1(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1: 
            return x
        isNegative  = n < 0
        if isNegative:
            n = -n
        res = x
        for i in range(n-1):
            res *= x
        
        return 1/res if isNegative else res

print(Solution().myPow(x = 2.00000, n = 5))

# Pow(x, n)

# Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

# Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

# You may not use any built-in library functions.

# Example 1:

# Input: x = 2.00000, n = 5

# Output: 32.00000
# Example 2:

# Input: x = 1.10000, n = 10

# Output: 2.59374
# Example 3:

# Input: x = 2.00000, n = -3

# Output: 0.12500
# Constraints:

# -100.0 < x < 100.0
# -1000 <= n <= 1000
# n is an integer.
# If x = 0, then n will be positive.
