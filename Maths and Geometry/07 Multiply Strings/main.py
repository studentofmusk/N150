class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1)+len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += digit
                res[i+j+1] += (res[i+j]//10)
                res[i+j] = res[i+j]%10
        
        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg+=1
        
        res = map(str, res[beg:])
        return "".join(res)

print(Solution().multiply(num1 = "3", num2 = "4"))

# Multiply Strings
# You are given two strings num1 and num2 that represent non-negative integers.

# Return the product of num1 and num2 in the form of a string.

# Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

# Note: You can not use any built-in library to convert the inputs directly into integers.

# Example 1:

# Input: num1 = "3", num2 = "4"

# Output: "12"
# Example 2:

# Input: num1 = "111", num2 = "222"

# Output: "24642"
# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
