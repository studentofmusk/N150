from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numCount = [0] * 3
        for num in nums:
            numCount[num]+=1
        i = 0
        for num, count in enumerate(numCount):
            for _ in range(count):
                nums[i] = num
                i+=1
    
    # With Three Pointer I 
    def sortColors2(self, nums: List[int]) -> None:
        
        l, r = 0, len(nums)-1
        i = l
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i<=r:
            if nums[i] == 0:
                swap(l, i)
                l+=1
            elif nums[i] == 2:
                swap(r, i)
                r-=1
                i-=1
            
            i+=1

    # With Three Pointer II 
    def sortColors3(self, nums: List[int]) -> None:
        zero = one = two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0

                two+=1
                one+=1
                zero+=1

            elif nums[i] == 1:
                nums[two] = 2
                nums[one] = 1

                two+=1
                one+=1

            else:
                nums[two] = 2
                two+=1
                
                
case1 = [1,0,1,2]
Solution().sortColors2(case1)
print(case1)

case1 = [1,0,1,2]
Solution().sortColors3(case1)
print(case1)

# Sort Colors
# Solved 
# You are given an array nums consisting of n elements where each element is an integer representing a color:

# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

# You must not use any built-in sorting functions to solve this problem.

# Example 1:

# Input: nums = [1,0,1,2]

# Output: [0,1,1,2]
# Example 2:

# Input: nums = [2,1,0]

# Output: [0,1,2]
# Constraints:

# 1 <= nums.length <= 300.
# 0 <= nums[i] <= 2.
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

