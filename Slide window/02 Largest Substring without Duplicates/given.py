class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        letters:set[str] = set()
        l = 0

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l+=1
            
            letters.add(s[r])
            res = max(res, r-l+1)
        return res



class Solution1:
    def lengthOfLongestSubstring(self, s):
        res = 0
        l = r = 0
        n = len(s)
        letters = set()

        while r < n:
            while r < n and s[r] not in letters:
                letters.add(s[r])
                r += 1
            res = max(len(letters), res)

            if r < n:
                while s[r] in letters:
                    letters.discard(s[l])
                    l += 1

        return res

#  Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.