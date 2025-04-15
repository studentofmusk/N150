class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = r = 0
        hashSet = set()
        while l<=r and r < len(s):
            if r-l+1 <len(t):
                if s[r] in t:
                    hashSet.add(s[r])
                r+=1
                continue
            if s[l] not in t:
                if s[l] in hashSet:
                    hashSet.remove(s[l])
                l+=1
                continue
            
            if len(hashSet) == len(t):
                res = s[r:l+1] if res == ""  or len(res) > r-l+1 else res
                if s[l] in hashSet:
                    hashSet.remove(s[l])
                l+=1
            elif len(hashSet) != len(t):
                if s[r] in t:
                    hashSet.add(s[r])
                r+=1

            else:
                r+=1

        return res
     
solution = Solution()
print(solution.minWindow(s = "OUZODYXAZV", t = "XYZ"))

# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"

# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"

# Example 3:

# Input: s = "x", t = "xy"

# Output: ""

# Constraints:

#     1 <= s.length <= 1000
#     1 <= t.length <= 1000
#     s and t consist of uppercase and lowercase English letters.
