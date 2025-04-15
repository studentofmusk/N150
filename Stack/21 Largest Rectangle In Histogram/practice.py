from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        levels = set(sorted(heights))
        # print(heights)
        # print(levels)
        Max = 0
        for level in levels:
            state_max = 0
            for  val in heights:
                if val >= level:
                    state_max += level 
                else:
                    Max = max(state_max, Max)
                    state_max = 0
            Max = max(state_max, Max) 

                    

        return Max
solution = Solution()
print(solution.largestRectangleArea([7,1,7,2,2,4]))
print(solution.largestRectangleArea([1, 3, 7]))

# Largest Rectangle In Histogram

# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.

# Example 1:

# Input: heights = [7,1,7,2,2,4]

# Output: 8

# Example 2:

# Input: heights = [1,3,7]

# Output: 7
