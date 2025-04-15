from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        row = []
        
        data = [(position[i], speed[i]) for i in range(len(position))]
        data = sorted(data, key=lambda x:x[0], reverse=True)

        for i, (p, s) in enumerate(data):
            dist = target - p
            time = dist/s
            # time = time if dist % s == 0 else time +1
            # # print(i, p, s)
            # print(time)
            # continue
            
            if i != 0 and row[-1] >= time:
                continue
            else:
                row.append(time)
        # print(row)
            

        return len(row)
    
    
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


# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

#     position[i] is the position of the ith car (in miles)
#     speed[i] is the speed of the ith car (in miles per hour)

# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1

# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.