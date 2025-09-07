class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r-l+1) - maxf > k:
                count[s[r]] -= 1
                l+=1               
        return r-l+1
                    
                
           

solution = Solution()
print(solution.characterReplacement("XYYX", 2))
print(solution.characterReplacement(s = "AAABABB", k = 1))
print(solution.characterReplacement(s = "AAAA", k = 2))
print(solution.characterReplacement(s="ABAB", k=2))
