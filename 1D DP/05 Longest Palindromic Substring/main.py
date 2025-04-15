from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        MAX = 0
        res = ""
        for i in range(len(s)):
            l = r = i
            # Odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > MAX:
                    res = s[l:r+1]
                    MAX = r-l+1
                r+=1
                l-=1

            l, r = i, i+1
            # Even
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > MAX:
                    MAX = r-l+1
                    res = s[l:r+1]
                r += 1
                l -= 1


        return res


print(Solution().longestPalindrome(s = "ababd"))
# Longest Palindromic Substring
#
# Given a string s, return the longest substring of s that is a palindrome.
#
# A palindrome is a string that reads the same forward and backward.
#
# If there are multiple palindromic substrings that have the same length, return any one of them.
#
# Example 1:
#
# Input: s = "ababd"
#
# Output: "bab"
#
# Explanation: Both "aba" and "bab" are valid answers.
#
# Example 2:
#
# Input: s = "abbc"
#
# Output: "bb"
#
# Constraints:
#
#     1 <= s.length <= 1000
#     s contains only digits and English letters.
#
