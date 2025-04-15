class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax  = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax  = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax  = leftMin - 1, leftMax + 1

            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False

        return leftMin == 0



print(Solution().checkValidString("((**)"))
print(Solution().checkValidString(s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
# Valid Parenthesis String
# You are given a string s which contains only three types of characters: '(', ')' and '*'.
#
# Return true if s is valid, otherwise return false.
#
# A string is valid if it follows all of the following rules:
#
# Every left parenthesis '(' must have a corresponding right parenthesis ')'.
# Every right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
# Example 1:
#
# Input: s = "((**)"
#
# Output: true
# Explanation: One of the '*' could be a ')' and the other could be an empty string.
#
# Example 2:
#
# Input: s = "(((*)"
#
# Output: false
# Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.
#
# Constraints:
#
# 1 <= s.length <= 100