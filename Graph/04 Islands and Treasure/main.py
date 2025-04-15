from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r, c):
            visit = set()
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            length = 1

            while queue :
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:

                        if(
                            min(r+dr, c+dc) < 0 or
                            r+dr == ROWS or c+dc == COLS or
                            grid[r+dr][c+dc] == -1 or
                            (r+dr, c+dc) in visit
                        ):
                            continue

                        if grid[r+dr][c+dc] == 0:
                            return length

                        visit.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))

                length += 1

            return length


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)




grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Solution().islandsAndTreasure(grid)
print(grid)


# Islands and Treasure
#
# You are given a m×nm×n 2D grid initialized with these three possible values:
#
#     -1 - A water cell that can not be traversed.
#     0 - A treasure chest.
#     INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
#
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.
#
# Assume the grid can only be traversed up, down, left, or right.
#
# Example 1:
#
# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
#
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
#
# Example 2:
#
# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]
#
# Output: [
#   [0,-1],
#   [1,2]
# ]
#
# Constraints:
#
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 100
#     grid[i][j] is one of {-1, 0, 2147483647}
