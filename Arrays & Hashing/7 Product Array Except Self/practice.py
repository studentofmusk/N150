from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        pre = 1
        for i in range(len(nums)):
            res.append(pre)
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res
    

solution = Solution()
print(solution.productExceptSelf([1, 2, 1, 2]))
print(solution.productExceptSelf([1,2,4,6]))
print(solution.productExceptSelf([-1,0,1,2,3]))

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]



# a = [1, 2, 1, 2]
# pre [1, 1, 2, 2, 4]
# post[4, 4, 2, 2, 1]

# ans [4, 2, 4, 2]