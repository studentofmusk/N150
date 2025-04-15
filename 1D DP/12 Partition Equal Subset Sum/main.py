from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)
        if SUM % 2 != 0:
            return False
        target = SUM / 2
        cache = {}
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == 0:
                return True
            if i >= len(nums) or total < 0:
                return False

            cache[(i, total)] = dfs(i+1, total - nums[i]) or dfs(i+1, total)
            return cache[(i, total)]

        return dfs(0, target)
    def dp(self, nums: List[int])-> bool:
        SUM = sum(nums)
        if SUM % 2 != 0:
            return  False

        target = SUM//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False

print(Solution().canPartition(nums = [8, 4, 10, 22]))
print(Solution().canPartition(nums = [1,2,3,4]))
print(Solution().dp(nums = [8, 4, 10, 22]))
print(Solution().dp(nums = [1,2,3,4]))


# Partition Equal Subset Sum
#
# You are given an array of positive integers nums.
#
# Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.
#
# Example 1:
#
# Input: nums = [1,2,3,4]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 4] and [2, 3].
#
# Example 2:
#
# Input: nums = [1,2,3,4,5]
#
# Output: false
#
# Constraints:
#
#     1 <= nums.length <= 100
#     1 <= nums[i] <= 50
#
