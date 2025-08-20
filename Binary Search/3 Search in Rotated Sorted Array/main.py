from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target: return mid

            elif nums[l] <= nums[mid]:
                # check left
                if nums[mid] < target or nums[l] > target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                # check right
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1
        return -1
    

nums=[3,4,5,6,1,2]
target=1
print(Solution().search(nums, target))
