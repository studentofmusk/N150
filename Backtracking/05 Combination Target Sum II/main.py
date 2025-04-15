from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if i == len(candidates):
                if total == target:
                    res.append(subset.copy())
                return

            if total > target:
                return

            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, total)



        dfs(0, 0)
        return res

print(Solution().combinationSum2(
candidates = [1,2,3,2], target = 4
))
print(Solution().combinationSum2(
candidates = [9,2,2,4,6,1,5], target = 8
))


# Combination Target Sum II
#
# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.
#
# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
#
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.
#
# Example 1:
#
# Input: candidates = [9,2,2,4,6,1,5], target = 8
#
# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]
#
# Example 2:
#
# Input: candidates = [1,2,3,4,5], target = 7
#
# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]
#
# Constraints:
#
#     1 <= candidates.length <= 100
#     1 <= candidates[i] <= 50
#     1 <= target <= 30
#
