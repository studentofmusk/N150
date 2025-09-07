class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Count, s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord("a")] += 1
            s2Count[ord(s2[i])-ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # print(s1Count)
        # print(s2Count)
        # print(matches)

        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 ==s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -=1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches-=1
            
            l+=1
        return matches == 26

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
