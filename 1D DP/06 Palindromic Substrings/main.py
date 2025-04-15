class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1)

        return res
    def countPali(self, s:str, l: int, r: int)->int:
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

print(Solution().countSubstrings(s="abc"))
print(Solution().countSubstrings(s="aaa"))
# Palindromic Substrings
#
# Given a string s, return the number of substrings within s that are palindromes.
#
# A palindrome is a string that reads the same forward and backward.
#
# Example 1:
#
# Input: s = "abc"
#
# Output: 3
#
# Explanation: "a", "b", "c".
#
# Example 2:
#
# Input: s = "aaa"
#
# Output: 6
#
# Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.
#
# Constraints:
#
#     1 <= s.length <= 1000
#     s consists of lowercase English letters.
#
