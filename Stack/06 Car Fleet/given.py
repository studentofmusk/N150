from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stact = []

        for p, s in sorted(pair)[::-1]:
            stact.append((target-p)/s)

            if len(stact)>=2 and stact[-1] <= stact[-2]:
                stact.pop()
        return len(stact)
    

      
solution = Solution()
print(solution.carFleet(10, [1,4], [3, 2]))
print(solution.carFleet(10, [4,1,0,7], [2,2,1,1]))
print(solution.carFleet(
    target=12,
    position=[10,8,0,5,3],
    speed=[2,4,1,1,3]
    ))
print(solution.carFleet(
    target=10,
    position=[6,8],
    speed=[3,2]
    ))
print(solution.carFleet(
    target=10,
    position=[8,3,7,4,6,5],
    speed=[4,4,4,4,4,4]
    ))


