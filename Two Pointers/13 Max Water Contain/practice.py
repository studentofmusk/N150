from typing import List
class Solution:
    def maxArea(self, heights:List[int]) -> int:
        m_area = 0
        i = 0
        j = len(heights)-1
        while (i < j):
            h = min(heights[i], heights[j])
            w = (j - i)
            m_area = max(h*w, m_area)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return m_area

solution = Solution()
print(solution.maxArea([1,7,2,5,4,7,3,6]))
print(solution.maxArea([2,2,2]))