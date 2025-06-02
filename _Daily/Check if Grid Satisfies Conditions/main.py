from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        def validate(row):
            prev = -1
            for ele in row:
                if prev == ele:
                    return False
                prev = ele
            return True 
        first = grid[0]  
        if not validate(first):
            return False

        return all(first == row for row in grid)