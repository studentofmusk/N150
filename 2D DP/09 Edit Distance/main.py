class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        cache = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            cache[i][N] = M - i

        for j in range(N):
            cache[M][j] = N - j

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i+1][j],
                        cache[i][j+1],
                        cache[i+1][j+1]
                    )
        return cache[0][0]
print(Solution().minDistance(word1 = "monkeys", word2 = "money"))
print(Solution().minDistance(word1 = "neatcdee", word2 = "neetcode"))
# Edit Distance
#
# You are given two strings word1 and word2, each consisting of lowercase English letters.
#
# You are allowed to perform three operations on word1 an unlimited number of times:
#
#     Insert a character at any position
#     Delete a character at any position
#     Replace a character at any position
#
# Return the minimum number of operations to make word1 equal word2.
#
# Example 1:
#
# Input: word1 = "monkeys", word2 = "money"
#
# Output: 2
#
# Explanation:
# monkeys -> monkey (remove s)
# monkey -> monkey (remove k)
#
# Example 2:
#
# Input: word1 = "neatcdee", word2 = "neetcode"
#
# Output: 3
#
# Explanation:
# neatcdee -> neetcdee (replace a with e)
# neetcdee -> neetcde (remove last e)
# neetcde -> neetcode (insert o)
#
# Constraints:
#
#     0 <= word1.length, word2.length <= 100
#     word1 and word2 consist of lowercase English letters.
#
