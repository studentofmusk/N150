from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(i+1)
        dfs(0)
        return res


print(Solution().subsetsWithDup([1, 2, 3, 2]))

# Subsets II
#
# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
#
# The solution must not contain duplicate subsets. You may return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,1]
#
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
#
# Example 2:
#
# Input: nums = [7,7]
#
# Output: [[],[7], [7,7]]
#
# Constraints:
#
#     1 <= nums.length <= 11
#     -20 <= nums[i] <= 20
#
