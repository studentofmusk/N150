from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]])->None:
        l, r = 0, len(matrix)-1

        while l<r:
            for i in range(r-l):
                top, bottom = l, r

                topLeft = matrix[top][l+i]

                # move bottom left to top left
                matrix[top][l+i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left value to top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1

    def solution_2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        res = [[0] * n for i in range(n)]

        for i in range(n):
            for j in range(n):
                res[j][n-1-i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]

matrix = [
[1,2],
[3,4]
]
Solution().rotate(matrix)
print(matrix)    

# Rotate Image
# Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

# You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

# Example 1:



# Input: matrix = [
#   [1,2],
#   [3,4]
# ]

# Output: [
#   [3,1],
#   [4,2]
# ]
# Example 2:



# Input: matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# Output: [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
