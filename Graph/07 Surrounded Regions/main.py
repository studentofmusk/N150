from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if(
                min(r, c) < 0 or
                r == ROWS or c == COLS
            ):
                visit.clear()
                return True

            if board[r][c] == "X" or (r, c) in visit:
                return False

            visit.add((r, c))

            res = (
                dfs(r+1, c) or
                dfs(r-1, c) or
                dfs(r, c+1) or
                dfs(r, c-1)
            )
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    if not dfs(r, c):
                        for tr, tc in visit:
                            board[tr][tc] = "X"


board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
Solution().solve(board)
print(board)

# Surrounded Regions
#
# You are given a 2-D matrix board containing 'X' and 'O' characters.
#
# If a continuous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.
#
# Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.
#
# Example 1:
#
# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]
# ]
#
# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]
#
# Explanation: Note that regions that are on the border are not considered surrounded regions.
#
# Constraints:
#
#     1 <= board.length, board[i].length <= 200
#     board[i][j] is 'X' or 'O'.
