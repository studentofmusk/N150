from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def count_pairs(max_dist: int) -> int:
            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_dist:
                    j += 1
                count += j - i - 1  # pairs (i, i+1 ... j-1)
            return count
        
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low


print(Solution().smallestDistancePair([1,2, 5, 6, 10, 25, 26], k=5))

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

# Example 1:

# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Example 2:

# Input: nums = [1,1,1], k = 2
# Output: 0
# Example 3:

# Input: nums = [1,6,1], k = 3
# Output: 5
 

# Constraints:

# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2