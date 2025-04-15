from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visit = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def dfs(r, c, prev):
            if (
                min(r, c) < 0 or
                r == ROWS or
                c == COLS or
                prev >= matrix[r][c]
            ):
                return 0

            if (r, c) in visit:
                return visit[(r, c)]


            visit[(r, c)] = 1 + max(
                dfs(r+1, c, matrix[r][c]),
                dfs(r-1, c, matrix[r][c]),
                dfs(r, c+1, matrix[r][c]),
                dfs(r, c-1, matrix[r][c])
            )
            return visit[(r, c)]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit:
                    res = max(res, dfs(r, c, float('-inf')))

        return res

    def memorization(self, matrix: List[List[int]]) -> int:
        def dfs(matrix, cache, i, j):
            if cache[i][j]: return cache[i][j]

            val = matrix[i][j]

            cache[i][j] = 1 + max(
                dfs(matrix, cache, i-1, j) if i > 0 and matrix[i-1][j] > val else 0,
                dfs(matrix, cache, i+1, j) if i <= m-2 and matrix[i+1][j] > val else 0,
                dfs(matrix, cache, i, j-1) if j > 0 and matrix[i][j-1] > val else 0,
                dfs(matrix, cache, i, j+1) if j <= n-2 and matrix[i][j+1] > val else 0
            )

            return cache[i][j]

        m, n = len(matrix), len(matrix[0])
        cache = [[0]*n for _ in range(m)]
        ans = max(dfs(matrix, cache, i, j) for j in range(n) for i in range(m))

        return ans



print(Solution().longestIncreasingPath(
    matrix = [[5,5,3],
              [2,3,6],
              [1,1,1]]
))
print(Solution().longestIncreasingPath(
    matrix=[[1,2,3],
            [2,1,4],
            [7,6,5]]
))
print(Solution().memorization(
    matrix = [[5,5,3],
              [2,3,6],
              [1,1,1]]
))
print(Solution().memorization(
    matrix=[[1,2,3],
            [2,1,4],
            [7,6,5]]
))


# Longest Increasing Path in Matrix
#
# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.
#
# Return the length of the longest strictly increasing path within matrix.
#
# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.
#
# Example 1:
#
# Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]
#
# Output: 4
#
# Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].
#
# Example 2:
#
# Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]
#
# Output: 7
#
# Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].
#
# Constraints:
#
#     1 <= matrix.length, matrix[i].length <= 100
#
