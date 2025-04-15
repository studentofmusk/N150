from typing import List
from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        i = len(digits)-1
        carry = 1
        while i >= 0:
            digit = digits[i] + carry
            carry =  digit // 10
            if carry:
                digit = digit % 10
            res.appendleft(digit)
            i-=1
        if carry:
            res.appendleft(carry)
        return list(res)
    
    def plusOne2(self, digits: List[int])->List[int]:
        if not digits:
            return [1]
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne2(digits[:-1]) + [0]
print(Solution().plusOne([1, 2, 3, 4]))
print(Solution().plusOne([9, 9, 9]))
print(Solution().plusOne2([1, 2, 3, 4]))
print(Solution().plusOne2([9, 9, 9]))

# Plus One
# You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

# Return the digits of the given integer after incrementing it by one.

# Example 1:

# Input: digits = [1,2,3,4]

# Output: [1,2,3,5]
# Explanation 1234 + 1 = 1235.

# Example 2:

# Input: digits = [9,9,9]

# Output: [1,0,0,0]
# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
