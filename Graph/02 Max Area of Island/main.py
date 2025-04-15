from itertools import count
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, dfs(r, c))

        return res

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
print(Solution().maxAreaOfIsland(grid))

# Max Area of Island
#
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
#
# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is defined as the number of cells within the island.
#
# Return the maximum area of an island in grid. If no island exists, return 0.
#
# Example 1:
#
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
#
# Output: 6
#
# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
#
# Constraints:
#
#     1 <= grid.length, grid[i].length <= 50
