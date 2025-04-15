from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        elements = set()
        for num in nums:
            if num in elements:
                return num
            elements.add(num)
        return -1
    def given(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

solution = Solution()
print(solution.given([1, 3, 4, 2, 2]))
print(solution.findDuplicate([1, 3, 4, 2, 2]))

# Find Duplicate Integer
#
# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
#
# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
#
# Example 1:
#
# Input: nums = [1,2,3,2,2]
#
# Output: 2
#
# Example 2:
#
# Input: nums = [1,2,3,4,4]
#
# Output: 4
#
# Follow-up: Can you solve the problem without modifying the array nums and using O(1)O(1) extra space?
#
# Constraints:
#
#     1 <= n <= 10000
#     nums.length == n + 1
#     1 <= nums[i] <= n
