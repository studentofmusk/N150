from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    if(
                        min(r+dr, c+dc) < 0 or
                        r+dr == ROWS or c+dc == COLS or
                        grid[r+dr][c+dc] != 1
                    ):
                        continue
                    queue.append((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1





grid = [[1,1,0],[0,1,1],[0,1,2]]
print(Solution().orangesRotting(grid))
grid = [[1,0,1],[0,2,0],[1,0,1]]
print(Solution().orangesRotting(grid))
grid=[[2,1,1],
      [0,1,1],
      [1,0,1]]
print(Solution().orangesRotting(grid))
grid=[[2,1,1],
      [1,1,1],
      [0,1,2]]
print(Solution().orangesRotting(grid))
grid = [[0, 2]]
print(Solution().orangesRotting(grid))
grid=[[0]]
print(Solution().orangesRotting(grid))



# You are given a 2-D matrix grid. Each cell can have one of three possible values:
#
#     0 representing an empty cell
#     1 representing a fresh fruit
#     2 representing a rotten fruit
#
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
#
# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
#
# Example 1:
#
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
#
# Output: 4
#
# Example 2:
#
# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
#
# Output: -1
#
# Constraints:
#
#     1 <= grid.length, grid[i].length <= 10
#
