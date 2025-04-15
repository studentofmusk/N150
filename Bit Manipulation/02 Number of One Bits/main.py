class Solution:
    def hammingWeight(self, n: int) -> int:
         
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        
        return res
    def hammingWeight1(self, n: int) -> int:
        temp = n 
        res = 0
        while temp != 0:
            res += temp%2
            temp = temp >> 1
        
        return res


print(Solution().hammingWeight(
     n = 0b00000000000000000000000000010111
))


# Number of One Bits
# You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

# You may assume n is a non-negative integer which fits within 32-bits.

# Example 1:

# Input: n = 00000000000000000000000000010111

# Output: 4
# Example 2:

# Input: n = 01111111111111111111111111111101

# Output: 30