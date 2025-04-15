from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp =  ["".join(sorted(x)) for x in strs]
        h = {}
        for i in range(len(strs)):
            if temp[i] in h:
                h[temp[i]].append(strs[i])
            else:
                h[temp[i]] = [strs[i]]
        return list(h.values())

solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]

# Example 3:

# Input: strs = [""]

# Output: [[""]]