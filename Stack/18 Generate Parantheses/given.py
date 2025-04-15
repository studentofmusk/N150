from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN:int, closeN:int):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)
        return res
solution = Solution()
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(3))



# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]

# Example 2:

# Input: n = 3

# Output: ["((()))","(()())","(())()","()(())","()()()"]
