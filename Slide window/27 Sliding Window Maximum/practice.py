from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(nums[i:i+k]))

        return res

solution = Solution()
print(solution.maxSlidingWindow(nums=[1,2,1,0,4,2,6], k = 3))

# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

# Constraints:

#     1 <= nums.length <= 1000
#     -1000 <= nums[i] <= 1000
#     1 <= k <= nums.length

