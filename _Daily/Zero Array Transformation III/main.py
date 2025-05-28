from typing import List
import heapq
    
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums)+1)
        operations = 0
        j = 0

        for i, num in enumerate(nums):
            operations += deltaArray[i]
            
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j+=1
            
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[(-heapq.heappop(heap)+1)] -= 1
            
            if operations < num:
                return -1
        
        return len(heap)
    
print(Solution().maxRemoval([1, 3, 0, 2, 3], [[0, 1], [3, 3], [2, 2]]))