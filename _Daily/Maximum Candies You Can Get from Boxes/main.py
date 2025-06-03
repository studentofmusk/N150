from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        total_candies = 0
        owned = set(initialBoxes)
        opened = set()

        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
        
        while q:
            box = q.popleft()
            if box in opened:
                continue
            total_candies += candies[box]
            opened.add(box)
            
            for key in keys[box]:
                status[key] = 1
                if key in owned and key not in opened:
                    q.append(key)

            for new_box in containedBoxes[box]:
                owned.add(new_box)
                if status[new_box] == 1 and new_box not in opened:
                    q.append(new_box)

        return total_candies


