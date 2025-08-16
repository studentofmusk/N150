from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, 0, n-1)
        return nums

    def mergeSort(self, nums: List[int], s:int, e:int):

        if (e-s+1) <=1:
            return
        
        mid = (s+e)//2

        self.mergeSort(nums, s, mid)
        self.mergeSort(nums, mid+1, e)

        self.merge(nums, s, mid, e)

    
    def merge(self, nums:List[int], s:int, mid:int, e:int):
        res = []
        i, j = s, mid+1
        while i<=mid and j<=e:
            if nums[i]<= nums[j]:
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        
        while i <= mid:
            res.append(nums[i])
            i+=1
        while j <= e:
            res.append(nums[j])
            j+=1
        
        nums[s:e+1] = res
    
        
