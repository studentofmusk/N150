from typing import List
# This program gives avg : 2900 ms for exec but we have below optimized solution which can avg run speed in 108 ms
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if i == len(word): return True
            if (
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS or
                word[i] != board[r][c] or
                (r, c) in visit
            ):
                return False

            visit.add((r, c))

            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            visit.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

print(Solution().exist(board, word))

"""
# Optimized Solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, o = len(board), len(board[0]), len(word)
        
        def deep_copy(visited):
            out = set()
            for e in visited:
                out.add(tuple(e))
            return out
        
        def bfs(i, j):
            words, visited, s = {}, {(i,j)}, board[i][j]
            q = [[i, j, s, 1, visited]]
            while q:
                new_q = []
                for six in q:
                    i, j, s, k, v = six

                    if s in words and words[s] == m*n:
                        break
            
                    words[s] = words.get(s,0) + 1

                    if s == word:
                        return True

                    if (i+1 < m) and (board[i+1][j] == word[k]) and ((i+1,j) not in v):
                        nv = deep_copy(v)
                        nv.add( (i+1, j) )
                        new_q.append( [ i+1, j, s+board[i+1][j], k+1, nv ] )

                    if (i-1 >= 0) and (board[i-1][j] == word[k]) and ((i-1,j) not in v):
                        nv = deep_copy(v)
                        nv.add( (i-1, j) )
                        new_q.append( [ i-1, j, s+board[i-1][j], k+1, nv ] )

                    if (j+1 < n) and (board[i][j+1] == word[k]) and ((i,j+1) not in v):
                        nv = deep_copy(v)
                        nv.add( (i, j+1) )
                        new_q.append( [ i, j+1, s+board[i][j+1], k+1, nv ] )

                    if (j-1 >= 0) and (board[i][j-1] == word[k]) and ((i,j-1) not in v):
                        nv = deep_copy(v)
                        nv.add( (i, j-1) )
                        new_q.append( [ i, j-1, s+board[i][j-1], k+1, nv ] )
                q = new_q
            return -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                   found = bfs(i, j)
                   if found == True:
                       return True
        return False 
"""

# Search for Word
#
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
#
# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
#
# Example 1:
#
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
#
# Output: true
#
# Example 2:
#
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
#
# Output: false
#
# Constraints:
#
#     1 <= board.length, board[i].length <= 5
#     1 <= word.length <= 10
#     board and word consists of only lowercase and uppercase English letters.
#
