class Solution:
    @staticmethod
    def longestCommonSubstr(s1: str, s2: str)->int:
        
        dp = [0] * (len(s1)+1)
        res = 0
        for char_2 in s2:
            temp = [0] * (len(s1)+1)
            for i in range(1, len(s1)+1):
                char_1 = s1[i-1]
                if char_1 == char_2:
                    temp[i] = dp[i-1] + 1

            dp = temp
            res = max(res, max(dp))

        return res
    
test_cases = [
    {"s1": "GeeksforGeeks", "s2": "GeeksQuiz"},
    {"s1": "abcdxyz", "s2": "xyzabcd"},
    {"s1": "abc", "s2": ""},

]
for test in test_cases:
    print(Solution.longestCommonSubstr(**test))
