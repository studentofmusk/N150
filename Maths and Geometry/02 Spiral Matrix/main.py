from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])-1
        top, bottom =0,  len(matrix)-1

        res = []

        while l<=r and top <= bottom:
            for i in range(l, r+1):
                res.append(matrix[top][i])

            for i in range(top+1, bottom+1):
                res.append(matrix[i][r])

            
            if top < bottom:    
                for i in range(r-1, l-1, -1):
                    res.append(matrix[bottom][i])
            if l<r:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][l])
            
            r -=1
            l +=1
            top +=1
            bottom -=1
        return res

print(Solution().spiralOrder(
    matrix = [[1,2],[3,4]]
))

print(Solution().spiralOrder(
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
))
# Spiral Matrix
# Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

# Example 1:



# Input: matrix = [[1,2],[3,4]]

# Output: [1,2,4,3]
# Example 2:



# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Output: [1,2,3,6,9,8,7,4,5]
# Example 3:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Constraints:

# 1 <= matrix.length, matrix[i].length <= 10
# -100 <= matrix[i][j] <= 100
