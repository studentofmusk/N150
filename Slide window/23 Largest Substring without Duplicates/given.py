class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(r-l+1, res)

        return res
    
solution = Solution()
print(solution.lengthOfLongestSubstring("zxyzxyz"))
print(solution.lengthOfLongestSubstring("xxxx"))
print(solution.lengthOfLongestSubstring("abcabcbb"))
