from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack:list[int] = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ast = 0
                else:
                    ast = 0
                    stack.pop()

            if ast:
                stack.append(ast)
        return stack

class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack:list[int] = []

        for asteroid in asteroids:
            if stack and (asteroid < 0 and stack[-1] > 0):
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroid):
                    continue
                else:
                    insert = True
                    while stack and insert and (asteroid < 0 and stack[-1] > 0):
                        if abs(stack[-1]) == abs(asteroid):
                            stack.pop()
                            insert = False
                        elif abs(stack[-1]) > abs(asteroid):
                            insert = False
                        else:
                            stack.pop()

                    if insert:
                        stack.append(asteroid)
                            
                        
            else:
                stack.append(asteroid)
        
        return stack

# Asteroid Collision
# Solved 
# You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Example 1:

# Input: asteroids = [2,4,-4,-1]

# Output: [2]
# Example 2:

# Input: asteroids = [5,5]

# Output: [5,5]
# Example 3:

# Input: asteroids = [7,-3,9]

# Output: [7,9]
# Constraints:

# 2 <= asteroids.length <= 10,000.
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
