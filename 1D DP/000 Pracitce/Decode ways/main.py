from time import perf_counter
from functools import lru_cache
class Solution:
    
    def decodeways(self, s: str) -> int:
        codes = set([str(i) for i in range(1, 27)])
        n = len(s)

        @lru_cache
        def dfs(index):
            
            if index == n:
                return 1

            res = 0

            if s[index] in codes:
                res += dfs(index + 1)
            if s[index:index+2] in codes and len(s[index:index+2]) == 2:
                res += dfs(index + 2)
            return res
            
                
        return dfs(0)
    

    def dp_sol(self,s:str):
        codes = set([str(i) for i in range(1, 27)])
        def isValid(digit:str)->bool:
            return digit in codes

        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]

            if isValid(s[i-2:i]):
                dp[i] += dp[i-2]

        return dp[n]
    
n = "112"
start = perf_counter()
print(Solution().decodeways(n))
end = perf_counter()
print(f"Time Taken: {(end-start)*1000:.4f}ms" )

start = perf_counter()
print(Solution().dp_sol(n))
end = perf_counter()

print(f"Time Taken: {(end-start)*1000:.4f}ms" )
        
"""
    Let 1 maps to 'A', 2 maps to 'B', ..., 26 to 'Z'. Given a digit sequence, count the number of possible decodings of the given digit sequence. 

    Consider the input string "123". There are three valid ways to decode it:

    "ABC": The grouping is (1, 2, 3) → 'A', 'B', 'C'
    "AW": The grouping is (1, 23) → 'A', 'W'
    "LC": The grouping is (12, 3) → 'L', 'C'

    Note: Groupings that contain invalid codes (e.g., "0" by itself or numbers greater than "26") are not allowed.
    For instance, the string "230" is invalid because "0" cannot stand alone, and "30" is greater than "26", so it cannot represent any letter. The task is to find the total number of valid ways to decode a given string.

    EG.1
    Input: digits = "121"
    Output: 3
    Explanation: The possible decodings are "ABA", "AU", "LA"
"""