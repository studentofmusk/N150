from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        trie = Trie()

        for word in wordDict:
            trie.insert(word)
        

        def backtrack(i, stack):
            if i == len(s):
                res.append(
                    " ".join(stack)
                )
                return
            
            word = []
            curr = trie.root
            for j in range(i, len(s)):
                char = s[j]
                if char not in curr.children:
                    break
                
                word.append(char)
                curr = curr.children[char]

                if curr.endOfWord:
                    stack.append("".join(word))
                    backtrack(j+1, stack)
                    stack.pop()
                

        backtrack(0, [])
        return res
    

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        def backtrack(i, stack):
            if i == len(s):
                res.append(
                    " ".join(stack)
                )
                return
            

            for word in wordDict:
                if word == s[i:i+len(word)]:
                    stack.append(word)
                    backtrack(i+len(word), stack)
                    stack.pop()
            
            return
        
        backtrack(0, [])
        return res
                



# Word Break II
# Solved 
# You are given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "neetcode", wordDict = ["neet","code"]

# Output: ["neet code"]
# Example 2:

# Input: s = "racecariscar", wordDict = ["racecar","race","car","is"]

# Output: ["racecar is car","race car is car"]
# Example 3:

# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

# Output: []
# Constraints:

# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 100,000.
