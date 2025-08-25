from typing import List
from functools import lru_cache
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]

        curr.endOfWord = True
     
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for word in dictionary:
            self.insert(word)

        n = len(s)
        res = n
        
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            
            res = 1 + dfs(i+1)
            
            node = self.root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.endOfWord:
                    res = min(res, dfs(j+1))
            
            return res
        
        return dfs(0)

print(Solution().minExtraChar(
    "neetcode",
    ["neet","code","neetcode"]
))