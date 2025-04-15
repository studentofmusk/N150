from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_set = set()
        col_set = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        for row in row_set:
            for i in range(COLS):
                matrix[row][i] = 0
                

        for col in col_set:
            for i in range(ROWS):
                matrix[i][col] = 0
matrix = [
  [0,1],
  [1,0]
]
Solution().setZeroes(matrix)
print(matrix)
# Set Matrix Zeroes
# Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

# You must update the matrix in-place.

# Follow up: Could you solve it using O(1) space?

# Example 1:



# Input: matrix = [
#   [0,1],
#   [1,0]
# ]

# Output: [
#   [0,0],
#   [0,0]
# ]
# Example 2:



# Input: matrix = [
#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
# ]

# Output: [
#   [1,0,3],
#   [0,0,0],
#   [6,0,8]
# ]
# Constraints:

# 1 <= matrix.length, matrix[0].length <= 100
# -2^31 <= matrix[i][j] <= (2^31) - 1