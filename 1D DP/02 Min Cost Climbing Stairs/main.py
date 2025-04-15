from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        def dfs(i):
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            left = dfs(i+1)
            right = dfs(i+2)
            cache[i] = cost[i] + min(left, right)
            return cache[i]

        return min(dfs(0), dfs(1))

    def dps(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])

print(Solution().minCostClimbingStairs(cost = [1,2,3]))
print(Solution().minCostClimbingStairs(cost = [1,2,1,2,1,1,1]))
# Min Cost Climbing Stairs
#
# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
#
# You may choose to start at the index 0 or the index 1 floor.
#
# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
#
# Example 1:
#
# Input: cost = [1,2,3]
#
# Output: 2
#
# Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.
#
# Example 2:
#
# Input: cost = [1,2,1,2,1,1,1]
#
# Output: 4
#
# Explanation: Start at index = 0.
#
#     Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
#     Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
#     Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
#     Pay the cost of cost[6] = 1 and take one step to reach the top.
#     The total cost is 4.
#
# Constraints:
#
#     2 <= cost.length <= 100
#     0 <= cost[i] <= 100
#
