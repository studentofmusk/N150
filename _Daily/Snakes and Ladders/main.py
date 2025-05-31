from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def unwrap(grid):
            n = len(grid)
            res = []
            for i in range(n):
                r = n - i - 1
                if i % 2 == 0:
                    res.extend(grid[r])
                else:
                    for j in range(n):
                        c = n - j - 1
                        res.append(grid[r][c])
            return res

        path = unwrap(board)  # <- MUST be before the loop
        q = deque([(0, 0)])   # (index, moves)
        visit = set()
        n = len(board)
        end = n * n - 1

        while q:
            idx, moves = q.popleft()
            if idx == end:
                return moves

            for dice in range(1, 7):
                next_idx = idx + dice
                if next_idx > end:
                    continue

                dest = path[next_idx]
                if dest != -1:
                    dest -= 1
                else:
                    dest = next_idx

                if dest not in visit:
                    visit.add(dest)
                    q.append((dest, moves + 1))

        return -1
