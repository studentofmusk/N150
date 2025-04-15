class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == "*":
                cache[(i, j)] = (
                    (match and dfs(i+1, j)) or     # use *
                    dfs(i, j+2)  # don't use *
                )
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
    def dp(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        cache[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j+1 < len(p) and p[j+1] == "*":
                    cache[i][j] = cache[i][j+2]
                    if match:
                        cache[i][j] = (
                            cache[i+1][j] or
                            cache[i][j]
                        )
                elif match:
                    cache[i][j] = cache[i+1][j+1]
        return cache[0][0]

print(Solution().isMatch("aaa", "a*"))
print(Solution().isMatch("aaa", "c*a*b"))
print(Solution().isMatch("aaaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*b"))
print(Solution().dp("aaa", "a*"))
print(Solution().dp("aaa", "c*a*b"))
print(Solution().dp("aaaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*b"))
# Regular Expression Matching
#
# You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.
#
# Return true if the pattern matches the entire input string, otherwise return false.
#
#     '.' Matches any single character
#     '*' Matches zero or more of the preceding element.
#
# Example 1:
#
# Input: s = "aa", p = ".b"
#
# Output: false
#
# Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.
#
# Example 2:
#
# Input: s = "nnn", p = "n*"
#
# Output: true
#
# Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.
#
# Example 3:
#
# Input: s = "xyz", p = ".*z"
#
# Output: true
#
# Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".
#
# Constraints:
#
#     1 <= s.length <= 20
#     1 <= p.length <= 20
#     Each appearance of '*', will be preceded by a valid character or '.'.
