class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        l = 0
        state = []
        for r in range(len(s2)):
            if len(state) == 0 and len(s1) > len(s2[l:]):
                return False
            if l == r:
                if s2[l] in s1:
                    state.append(s2[l])
                else:
                    l+=1
                    continue
            elif s2[r] in s1:
                if s2[r] not in state:
                    state.append(s2[r])
                    
                else:
                    while l<r:
                        l+=1
                        if state:
                            if s2[r] == state[r-l-1]:
                                break
                            state.pop(0)
            else:
                l=r
                state = []
            
            if len(state) == len(s1):
                return True
                        
        return res


solution = Solution()
print(solution.checkInclusion( s1 = "abc", s2 = "lecabce"))
print(solution.checkInclusion( s1 = "abc", s2 = "lecaabee"))
print(solution.checkInclusion( s1="ab", s2="eidbaooo"))
print(solution.checkInclusion( s1="a", s2="ab"))
print(solution.checkInclusion( s1="adc", s2="dcda"))
print(solution.checkInclusion( s1="abc", s2="ccccbbbbaaaa"))
print(solution.checkInclusion( s1="industry", s2="interest"))
print(solution.checkInclusion( 
    s1 = "abcdxabcde", s2 = "abcdeabcdx"
))

# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true

# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false
