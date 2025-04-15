from typing import List     
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            if target-num in h.keys():
                return [h[target-num], idx]
            h[num] = idx
        return []
    
solution = Solution()
print(solution.twoSum([3,4,5,6], 7))

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]

# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
