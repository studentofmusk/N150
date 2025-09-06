from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(projects)

        available = []
        for _ in range(k):            
            while projects and projects[0][0] <= w:
                cap, profit = heapq.heappop(projects)
                heapq.heappush(available, -profit)
            
            if not available:
                return w
            
            w -= heapq.heappop(available)
        return w
                

# IPO
# Solved 
# A company has limited resources, it can only finish at most k distinct projects before the IPO. Help the company to design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it. Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.

# Example 1:

# Input: k = 3, w = 0, profits = [1,4,2,3], capital = [0,3,1,1]

# Output: 8
# Explanation : The order of indices to pick are [0,3,1] and final capital is (1 + 3 + 4) = 8.

# Example 2:

# Input: k = 4, w = 2, profit = [2,3,1,5,3], capital = [4,4,2,3,3]

# Output: 14
# Explanation: The order of indices to pick are [2,3,4,1] and final capital is (2 + (1 + 5 + 3 + 3)) = 14.

# Constraints:

# n == profits.length == capital.length
# 1 <= n, k <= 100,000
# 0 <= w <= 1,000,000,000
# 0 <= profits[i] <= 10,000
# 0 <= capital[i] <= 1,000,000,000
