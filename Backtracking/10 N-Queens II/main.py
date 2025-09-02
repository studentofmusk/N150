class Solution:
    def totalNQueens(self, n: int) -> int:
        leftCross = set()
        rightCross = set()
        cols = set()

        def backtrack(r, c):
            if (
                c in cols or 
                r-c in rightCross or 
                r+c in leftCross
            ):
                return 0

            if r >= n-1:
                return 1

            cols.add(c)
            leftCross.add(r+c)
            rightCross.add(r-c)
            
            res = 0
            for next_c in range(n):

                res += backtrack(r+1, next_c)
            
            cols.remove(c)
            leftCross.remove(r+c)
            rightCross.remove(r-c)
            
            return res
        

        res = 0
        for c in range(n):
            res += backtrack(0, c)
        
        return res


# N-Queens II
# Solved 
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# You are given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:

# Input: n = 4

# Output: 2
# Explanation: There are two different solutions to the 4-queens puzzle.

# Example 2:

# Input: n = 1

# Output: 1
# Constraints:

# 1 <= n <= 9
