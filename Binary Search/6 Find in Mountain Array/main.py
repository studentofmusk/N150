class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l, r = 0, mountainArr.length()-1
        peak = self.findPeak(mountainArr)

        left_search = self.bsearch(l, peak, target, mountainArr)
        
        if left_search != -1:
            return left_search

        right_search = self.bsearchReverse(peak, r, target, mountainArr)

        if right_search != -1:
            return right_search

        return -1

    def findPeak(self, mountain):
        l, r = 0, mountain.length()-1
        while l<r:
            mid = (r+l)//2

            mid_val = mountain.get(mid)
            right_val = mountain.get(mid+1)

            if mid_val < right_val:
                l = mid+1
            else:
                r = mid
        return l
            
        

    def bsearch(self, start, end, target, mountain):
        l, r = start, end
        while l<=r:
            mid = (l+r)//2
            
            mid_val = mountain.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                r = mid-1
            else:
                l = mid+1
            
        return -1
    
    def bsearchReverse(self, start, end, target, mountain):
        
        l, r = start, end
        
        while l<=r:
            mid = (l+r)//2

            mid_val = mountain.get(mid)

            if mid_val == target:
                return mid
            elif mid_val > target:
                l = mid+1
            else:
                r = mid-1
            
        return -1
        

# Find in Mountain Array
# Solved 
# (This problem is an interactive problem.)

# An array arr is called a mountain array if and only if:

# arr.length >= 3
# There exists some index i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# You are given a mountain array mountainArr and an integer target, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# You can only make at most 100 calls to the function get(). Submissions making more than 100 calls will be judged as Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

# Example 1:

# Input: mountainArr = [2,4,5,2,1], target = 2

# Output: 0
# Example 2:

# Input: mountainArr = [1,2,3,4,2,1], target = 6

# Output: -1
# Constraints:

# 3 <= mountainArr.length() <= 10,000
# 0 <= target, mountainArr.get(index) <= 1,000,000,000
