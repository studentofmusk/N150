from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l, r = 1, res

        while l <= r:
            rate = (r+l)//2

            hours = sum(math.ceil(p/rate) for p in piles)

            if hours <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res
