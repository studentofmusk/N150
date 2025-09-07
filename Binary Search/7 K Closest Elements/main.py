from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr)-k

        while l<r:
            mid = (r+l)//2

            if x-arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid
            
        return arr[l:l+k]
class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        index = self.bsearch(arr, x)
            
            
        l, r = index, index+1
		
        while k > 0:
            if l < 0:
                r+=1
            elif r >= n:
                l -= 1
            elif  abs(x - arr[l]) <= abs(arr[r] - x):
                l -= 1
            else:
                r+=1
            k -= 1
        
        return arr[l+1:r]
    
    def bsearch(self, arr, x):
        
        l, r = 0, len(arr)-1
        res = 0
        while l<=r:
            mid = (r+l)//2
            
            if arr[mid] > x:
                r = mid-1
            else:
                l = mid+1
                res = mid
            
        return res
    

# 658. Find K Closest Elements
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3

# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,1,2,3,4,5], k = 4, x = -1

# Output: [1,1,2,3]

 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104
