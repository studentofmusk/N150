from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i, j = 0, len(nums)-1
        while i+1 < j:
            k = j-1
            while k > i and j > k:
                threesum = nums[i]+ nums[k] + nums[j]
                if threesum == 0:
                    elements = [nums[i], nums[k], nums[j]] 
                    if elements not in res:
                        res.append(elements)

                    
                    k -= 1
                elif threesum < 0:
                    i +=1
                    k = j-1
                else:
                    k -=1
            j-=1
                   
        return res

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,0,0]))


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]

# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []

# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]

# Explanation: The only possible triplet sums up to 0.