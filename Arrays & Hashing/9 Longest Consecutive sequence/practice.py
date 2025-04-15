from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """This code works O(n^2)"""
        nums.sort()
        if len(nums) <=1 : return len(nums) 
        i, lng, blng = 1, 1, 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                i+=1
                continue
            if nums[i]-1 == nums[i-1]:
                lng += 1
            else:
                lng = 1
            if lng > blng:
                blng = lng
            i+=1
        return blng
solution = Solution()
print(solution.longestConsecutive([2,20,4,10,3,4,5]))
print(solution.longestConsecutive([0,3,2,5,4,6,1,1]))
print(solution.longestConsecutive([0,-1]))
# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
