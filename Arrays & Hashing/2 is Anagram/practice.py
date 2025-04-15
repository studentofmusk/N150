class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        i = 0
        while True:
            if len(s) > 0 and len(t) > 0:
                if t[i] in s:
                    pivot = s.index(t[i])
                    s = s[:pivot] + s[pivot+1:] 
                    t = t[:i]+t[i+1:]
                else:
                    return False
            else:
                if len(s) == len(t):
                    return True 
                else:
                    return False
         

solution = Solution()
print(solution.isAnagram("xx", "x"))
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
