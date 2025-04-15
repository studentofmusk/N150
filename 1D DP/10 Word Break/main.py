from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            for word in wordDict:
                if word == s[i:i+len(word)] and dfs(i+len(word)):
                    cache[i] = True
                    return cache[i]
            cache[i]  = False
            return cache[i]

        return dfs(0)


    def dp(self, s:str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break

        return dp[0]


# Memorization Top to Bottom
print(Solution().wordBreak("applepenapple", ["apple", "pen", "ape"]))
print(Solution().wordBreak(s="aaaaaaa", wordDict=["aaaa","aaa"]))
print(Solution().wordBreak(s="ab", wordDict=["a","b"]))

# Bottom Up
print(Solution().dp("applepenapple", ["apple", "pen", "ape"]))
print(Solution().dp(s="aaaaaaa", wordDict=["aaaa","aaa"]))
print(Solution().dp(s="ab", wordDict=["a","b"]))





# Word Break
#
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.
#
# You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
#
# Example 1:
#
# Input: s = "neetcode", wordDict = ["neet","code"]
#
# Output: true
#
# Explanation: Return true because "neetcode" can be split into "neet" and "code".
#
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
#
# Output: true
#
# Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.
#
# Example 3:
#
# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
#
# Output: false
#
# Constraints:
#
#     1 <= s.length <= 200
#     1 <= wordDict.length <= 100
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#
