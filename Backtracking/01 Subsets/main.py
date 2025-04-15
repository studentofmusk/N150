from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        if self.val > val:
            if self.left:
                self.left.add(val)
            else:
                self.left = TreeNode(val)
        elif self.val < val:
            if self.right:
                self.right.add(val)
            else:
                self.right = TreeNode(val)
        else:
            self.val = val


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

solution = Solution()
print(solution.subsets([1, 2, 3]))

#
# Subsets
#
# Given an array nums of unique integers, return all possible subsets of nums.
#
# The solution set must not contain duplicate subsets. You may return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
#
# Input: nums = [7]
#
# Output: [[],[7]]
#
# Constraints:
#
#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10
#
