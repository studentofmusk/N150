from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums

    def mergeSort(self, arr: List[int], start:int, end:int):
        if (end-start+1) <=1: return arr

        mid = (start+end)//2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid+1, end)

        self.merge(arr, start, mid, end)
        return arr

    def merge(self, arr: List[int], start:int, mid:int, end:int):
        res = []

        i = start
        j = mid+1

        while i <= mid and j<=end:
            if arr[i]<=arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        
        while i<=mid:
            res.append(arr[i])
            i+=1
        
        while j<=end:
            res.append(arr[j])
            j+=1

        arr[start:end+1] = res