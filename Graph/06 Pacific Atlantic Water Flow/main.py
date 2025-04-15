from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pas, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if(
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pas, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pas, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        return list(pas.intersection(atl))

heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
print(Solution().pacificAtlantic(heights))
heights=[[1],[1]]
print(Solution().pacificAtlantic(heights))

    
# Pacific Atlantic Water Flow
#
# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
#
# The islands border the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.
#
# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.
#
# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.
#
# Example 1:
#
# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
#
# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
#
# Example 2:
#
# Input: heights = [[1],[1]]
#
# Output: [[0,0],[0,1]]
#
# Constraints:
#
#     1 <= heights.length, heights[r].length <= 100
#     0 <= heights[r][c] <= 1000
#
