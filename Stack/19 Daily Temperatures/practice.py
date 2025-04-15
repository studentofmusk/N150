from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            isChange = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack.append(j-i)
                    isChange = True
                    break
            if isChange != True:
                stack.append(0)
        return stack


            

                 

solution = Solution()
print(solution.dailyTemperatures([30,38,30,36,35,40,28]))

# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]

# Example 2:

# Input: temperatures = [22,21,20]

# Output: [0,0,0]
