from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in range(1, len(matrix)):
            self.matrix[r][0] += self.matrix[r-1][0]
        
        for c in range(1, len(matrix[0])):
            self.matrix[0][c] += self.matrix[0][c-1]

        for r in range(1, len(self.matrix)):
            for c in range(1, len(self.matrix[0])):
                self.matrix[r][c] += (self.matrix[r-1][c]+self.matrix[r][c-1]-self.matrix[r-1][c-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_values = self.matrix[row1-1][col2] if row1 != 0 else 0
        left_values = self.matrix[row2][col1-1] if col1 != 0 else 0
        
        if col1 and row1:
            total_outliers = top_values + left_values - self.matrix[row1-1][col1-1]
        else:
            total_outliers = top_values + left_values

        return self.matrix[row2][col2]-total_outliers


matrix = [
    [1, 2, 1, 2],
    [2, 2, 1, 2], 
    [1, 1, 1, 1],
    [1, 1, 2, 1]
]
numMat = NumMatrix(matrix)

print(numMat.sumRegion(1, 1, 2, 2))
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)    


# Range Sum Query 2D Immutable
# Solved 
# You are given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.
# Example 1:

# Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]

# Output: [null, 8, 11, 12]
# Explanation:
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10,000 <= matrix[i][j] <= 10,000
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10,000 calls will be made to sumRegion.