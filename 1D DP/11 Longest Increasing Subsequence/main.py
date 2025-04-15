from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        res = 0
        def dfs(i):
            if i in cache:
                return cache[i]

            MAX = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    MAX = max(MAX, 1 + dfs(j))

            cache[i] = MAX
            return cache[i]

        for idx in range(len(nums)):
            res = max(res, dfs(idx))

        return res

    def dp(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)






print(Solution().lengthOfLIS(nums = [9,1,4,2,3,3,7]))
print(Solution().lengthOfLIS(nums = [0,3,1,3,2,3]))
print(Solution().dp(nums = [9,1,4,2,3,3,7]))
print(Solution().dp(nums = [0,3,1,3,2,3]))

# Longest Increasing Subsequence
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.
#
#     For example, "cat" is a subsequence of "crabt".
#
# Example 1:
#
# Input: nums = [9,1,4,2,3,3,7]
#
# Output: 4
#
# Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.
#
# Example 2:
#
# Input: nums = [0,3,1,3,2,3]
#
# Output: 4
#
# Constraints:
#
#     1 <= nums.length <= 1000
#     -1000 <= nums[i] <= 1000
#
