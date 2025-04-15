from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        i = 0
        while i < len(height)-1:
            if height[i] <= height[i+1]:
                i+=1
            else:
                mat = []
                j = i + 1
                while j < len(height):
                    if height[j] >= height[i]:
                        res.append(mat)
                        break
                    mat.append(height[j])
                    j+=1
                i+=1
        return res
 
            

solution = Solution()
print(solution.trap([3,1,0,1,3]))
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))


# You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:

# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
