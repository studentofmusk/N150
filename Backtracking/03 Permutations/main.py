from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res



solution = Solution()
print(solution.permute([1, 2, 3]))
# Permutations
#
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
#
# Input: nums = [7]
#
# Output: [[7]]
#
# Constraints:
#
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
