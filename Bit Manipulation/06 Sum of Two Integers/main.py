class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        max_int = 0x7fffffff
        
        while b:
            carry = (a&b) << 1 
            a = (a^b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a^mask)

        

print(Solution().getSum(30, 20))

# Sum of Two Integers
# Given two integers a and b, return the sum of the two integers without using the + and - operators.

# Example 1:

# Input: a = 1, b = 1

# Output: 2
# Example 2:

# Input: a = 4, b = 7

# Output: 11
# Constraints:

# -1000 <= a, b <= 1000
