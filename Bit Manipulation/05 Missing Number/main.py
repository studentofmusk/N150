from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i^nums[i]
        return xorr   
     
    def missingNumber2(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i-nums[i])
        return res
    
    

print(Solution().missingNumber([1,2,3]))

# Missing Number
# Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

# Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Example 1:

# Input: nums = [1,2,3]

# Output: 0
# Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

# Example 2:

# Input: nums = [0,2]

# Output: 1
# Constraints:

# 1 <= nums.length <= 1000