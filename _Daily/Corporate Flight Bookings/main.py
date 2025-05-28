from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dp = [0] * (n+2)
        for booking in bookings:
            dp[booking[0]] += booking[2]
            dp[booking[1]+1] -= booking[2]

        res = []
        operations = 0
        for delta in dp[1:-1]:
            operations += delta
            res.append(operations)
        
        return res
