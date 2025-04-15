from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.isWord = True

    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if(
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs < 1 or
                (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
"""class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if ( r < 0 or
                 c < 0 or
                 r == ROWS or
                 c == COLS or
                 board[r][c] not in node.children or
                 (r, c) in visit
                 ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)"""
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]

solution = Solution()
print(solution.findWords(board, words))
# Output: ["cat","back","backend"]

# Search for Word II
#
# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
#
# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
#
# Example 1:
#
# Input:
# board = [
#   ["a","b","c","d"],
#   ["s","a","a","t"],
#   ["a","c","k","e"],
#   ["a","c","d","n"]
# ],
# words = ["bat","cat","back","backend","stack"]
#
# Output: ["cat","back","backend"]
#
# Example 2:
#
# Input:
# board = [
#   ["x","o"],
#   ["x","o"]
# ],
# words = ["xoxo"]
#
# Output: []
#
# Constraints:
#
#     1 <= board.length, board[i].length <= 10
#     board[i] consists only of lowercase English letter.
#     1 <= words.length <= 100
#     1 <= words[i].length <= 10
#     words[i] consists only of lowercase English letters.
#     All strings within words are distinct.
#
