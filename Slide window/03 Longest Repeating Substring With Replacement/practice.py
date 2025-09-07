class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_l = 0
        k_l = []
        count = 0
        
        for r in range(1, len(s)):
            if s[r] == s[r-1] or (k_l and k_l[-1] == r-1):
                max_l = max(r-l+1, max_l)
            else:
                if k > count:
                    count += 1
                    k_l.append(r)
                    max_l = max(r-l+1, max_l)
                else:
                    l+=1
                    if k_l and l == k_l[0]:
                        count -=1 
                        k_l.pop(0)
                        k_l.append(r)
        return max_l 
                        
                    
                    
                
           

solution = Solution()
print(solution.characterReplacement("XYYX", 2))
print(solution.characterReplacement(s = "AAABABB", k = 1))
print(solution.characterReplacement(s = "AAAA", k = 2))
print(solution.characterReplacement(s="ABAB", k=2))

print("Wrong")
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.


# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4

# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
