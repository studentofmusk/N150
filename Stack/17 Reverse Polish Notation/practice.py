from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop()+stack.pop())
            elif ele == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif ele == "*":
                stack.append(stack.pop()*stack.pop())
            elif ele == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(ele))
        return stack[0]

            
solution = Solution()
print(solution.evalRPN(["1","2","+","3","*","4","-"]))

# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.

# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
