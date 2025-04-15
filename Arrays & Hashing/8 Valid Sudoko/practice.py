from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track horizontally and diagonally 
        diagonal_present = set()
        for i in range(9):
            present = set()
            box = board[i]
            for j in range(9):
                if i == j and box[j] != ".":
                    if box[j] in diagonal_present:
                        # print(diagonal_present)
                        # print("Diagonal issue!", box[j], (i, j))
                        return False
                    else:
                        diagonal_present.add(box[i])
                

                if box[j] in present and box[j] != ".":
                    # print("Row issue!")
                    return False
                    
                present.add(box[j])

            present.clear()
        diagonal_present.clear()

        # Track Vertically and Semi diagonally
        backward = 8
        for i in range(9):
            for j in range(9):
                if j == backward and board[j][i] != ".":
                    if  board[j][i] in diagonal_present:

                        # print("Semi Diagonal issue!")
                        return False
                    else:
                        diagonal_present.add(board[j][i])
                        backward -= 1

                if board[j][i] in present:
                    # print("Yes here")
                    # print("Column issue!")
                    return False
                elif board[j][i] != ".":
                    present.add(board[j][i])
            
            present.clear()
        
        del present
        del diagonal_present 
        return True
solution = Solution()
print(solution.isValidSudoku(
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","8",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","1",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]
))
print(solution.isValidSudoku(
    board=[["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [[".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".","3",".","."],
     [".",".",".","1","8",".",".",".","."],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".",".","1",".","9","7","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".","3","6",".","1",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","2","."]]
    ))


# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

#     Each row must contain the digits 1-9 without duplicates.
#     Each column must contain the digits 1-9 without duplicates.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true

# Example 2:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false

# Explanation: There are two 1's in the top-left 3x3 sub-box.