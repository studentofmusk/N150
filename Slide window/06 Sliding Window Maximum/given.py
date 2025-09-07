from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        q = deque() #Index
        l = r = 0
        while r < len(nums):
            # Pop the smallest value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output
    
solution = Solution()
print(solution.maxSlidingWindow(nums=[1,2,1,0,4,2,6], k = 3))
