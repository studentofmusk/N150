from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        res = []
        for i in range((len(s))):
            hashMap[s[i]] = i
        i = 0
        size = 0
        while i < len(s):
            ends = hashMap[s[i]]
            j = i
            while j <= ends:
                if hashMap[s[j]] > ends:
                    ends = hashMap[s[j]]
                size += 1
                j+=1
            res.append(size)
            size = 0
            i = ends+1
        return res
print(Solution().partitionLabels(s="xyxxyzbzbbisl"))

# 07 Partition Labels
# You are given a string s consisting of lowercase english letters.
#
# We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.
#
# Return a list of integers representing the size of these substrings in the order they appear in the string.
#
# Example 1:
#
# Input: s = "xyxxyzbzbbisl"
#
# Output: [5, 5, 1, 1, 1]
# Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].
#
# Example 2:
#
# Input: s = "abcabc"
#
# Output: [6]
# Constraints:
#
# 1 <= s.length <= 100
