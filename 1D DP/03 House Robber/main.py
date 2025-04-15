from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            if i >= len(nums) - 2:
                return nums[i]

            left = dfs(i+2)
            right = dfs(i+3)
            cache[i] = nums[i] + max(left, right)
            return cache[i]
        return max(dfs(0), dfs(1))

    def dps(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)-4, -1, -1):
            nums[i] = nums[i] + max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])

print(Solution().rob(nums=[5,1,2,10,6,2,7,9,3,1]))
print(Solution().dps(nums=[5,1,2,10,6,2,7,9,3,1]))

# House Robber
#
# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
#
# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
#
# Return the maximum amount of money you can rob without alerting the police.
#
# Example 1:
#
# Input: nums = [1,1,3,3]
#
# Output: 4
#
# Explanation: nums[0] + nums[2] = 1 + 3 = 4.
#
# Example 2:
#
# Input: nums = [2,9,8,3,6]
#
# Output: 16
#
# Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.
#
# Constraints:
#
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100
#
