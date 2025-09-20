from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        prev = None
        for num in nums:
            if prev is None:
                prev = num
            else:
                if prev == num:
                    prev = None
                else:
                    return prev
                
        return prev

class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                if len(seen) == 1:
                    return list(seen)[0]
                else:
                    seen.add(num)

        return list(seen)[0]
# 540. Single Element in a Sorted Array
# Medium
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
