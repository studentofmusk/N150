from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = candies[i+1] + 1
        return sum(candies)
    
    def candy1(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        dp = [1] * len(ratings)
        balanced = False
        while not balanced:
            balanced = True
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i-1]:
                    if dp[i] <= dp[i-1]:
                        dp[i] += 1
                        balanced = False
                    else:
                        continue
                elif ratings[i-1] > ratings[i]:
                    if dp[i-1] <= dp[i]:
                        dp[i-1] += 1
                        balanced = False
                    else:
                        continue
                else:
                    continue
        return sum(dp)


