from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs():
            res = 0
            ROWS, COLS = len(grid), len(grid[0])
            visit = set()
            dfs_visit = set()
            queue = deque()
            queue.append((0, 0))
            visit.add((0, 0))
            if grid[0][0] == "1":
                res += 1
                dfs(0, 0, dfs_visit, ROWS, COLS)


            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbours:
                        if (
                            min(r+dr, c+dc) < 0 or
                            r+dr == ROWS or
                            c+dc == COLS or
                            (r+dr, c+dc) in visit
                        ):
                            continue


                        if grid[r+dr][c+dc] == "1" and (r+dr, c+dc) not in dfs_visit:
                            res += 1
                            dfs(r+dr, c+dc, dfs_visit, ROWS, COLS)

                        visit.add((r + dr, c + dc))
                        dfs_visit.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))

            return res

        def dfs(r, c, visit, ROWS, COLS):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                grid[r][c] == "0"
            ):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, ROWS, COLS)
            dfs(r-1, c, visit, ROWS, COLS)
            dfs(r, c+1, visit, ROWS, COLS)
            dfs(r, c-1, visit, ROWS, COLS)

        return bfs()


    def given(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                grid[r][c] == "0" or
                (r, c) in visit
            ):
                return

            visit.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    res += 1
                    dfs(r, c)
        return res

grid1 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
grid2 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
grid3=[["1"]]

print(Solution().given(grid1))
print(Solution().given(grid2))
print(Solution().given(grid3))

# Count Number of Islands.

# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
#
# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
#
# Example 1:
#
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4
#
# Constraints:
#
#     1 <= grid.length, grid[i].length <= 100
#     grid[i][j] is '0' or '1'.
#
