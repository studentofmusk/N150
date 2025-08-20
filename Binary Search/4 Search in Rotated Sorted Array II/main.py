from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and l!=mid:
                l+=1
                continue
            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1 
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1
        return False

nums=[2,3,4,5,6,1,2,2,2]
target=1

print(Solution().search(nums, target))
print(Solution().search(nums, 9))
