from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        l, r = max(weights), sum(weights)
        res = r
        while l<=r:
            capacity = (l+r)//2
            days_took = self.ship(weights, capacity)
            if days_took <= days:
                res = capacity
                r = capacity-1
            else:
                l = capacity+1
        return res
    def ship(self, weights:List[int], capacity:int)->int:
        days = 1
        curr = 0
        for w in weights:
            if  curr + w > capacity:
                days+=1
                curr = 0
            curr += w 
        return days      


weights=[2,4,6,1,3,10]
days=4
print(Solution().shipWithinDays(weights, days))