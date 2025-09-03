from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:        

        def can_split(max_sum):
            count, curr = 1, 0
            for num in nums:
                if curr + num > max_sum:
                    curr = 0
                    count += 1
                curr += num

                if count > k:
                    return False
                
            return True
        
        l, r = max(nums), sum(nums)

        while l<r:
            mid = (l+r)//2

            if can_split(mid):
                r = mid
            else:
                l = mid+1
            
        return l


# Split Array Largest Sum
# Solved 
# You are given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [2,4,10,1,5], k = 2

# Output: 16
# Explanation: The best way is to split into [2,4,10] and [1,5], where the largest sum among the two subarrays is only 16.

# Example 2:

# Input: nums = [1,0,2,3,5], k = 4

# Output: 5
# Explanation: The best way is to split into [1], [0,2], [3] and [5], where the largest sum among the two subarrays is only 5.

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1,000,000
# 1 <= k <= min(50, nums.length)
