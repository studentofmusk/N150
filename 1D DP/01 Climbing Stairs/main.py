from tempfile import tempdir


class Solution:
    def climbStairs(self, n: int) -> int:

        def memorization(n: int, cache) -> int:
            if n < 2:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = memorization(n-1, cache) + memorization(n-2, cache)
            return cache[n]

        return memorization(n, {})

    def dps(self, n):
        if n < 2:
            return 1
        res = [1, 1]
        for i in range(2, n + 1):  # Loop should go until n (not n-1)
            temp = res[1]
            res[1] = res[0] + res[1]
            res[0] = temp

        return res[1]

    def dps2(self, n):
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one+two
            two = temp

        return one




print("DP Top to Bottom")
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))
print("DP-1 Bottom Up")
print(Solution().dps(2))
print(Solution().dps(3))
print(Solution().dps(5))

print("DP-2 Bottom Up")
print(Solution().dps(2))
print(Solution().dps(3))
print(Solution().dps(5))
# Climbing Stairs
#
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.
#
# Example 1:
#
# Input: n = 2
#
# Output: 2
#
# Explanation:
#
#     1 + 1 = 2
#     2 = 2
#
# Example 2:
#
# Input: n = 3
#
# Output: 3
#
# Explanation:
#
#     1 + 1 + 1 = 3
#     1 + 2 = 3
#     2 + 1 = 3
#
# Constraints:
#
#     1 <= n <= 30
#