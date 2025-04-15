class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        l = 0
        max_s = 1
        for r in range(1, len(s)):
            if s[r] in s[l:r]:
                while l < r:
                    if s[l] == s[r]:
                        l+=1
                        break
                    l = l+1
            else:
                max_s = max(r-l+1, max_s)
                        
        return max_s

solution = Solution()
print(solution.lengthOfLongestSubstring("zxyzxyz"))
print(solution.lengthOfLongestSubstring("xxxx"))
print(solution.lengthOfLongestSubstring("abcabcbb"))

# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3

# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
