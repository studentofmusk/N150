from typing import List
from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def find_evens(edges, n):

            evens = [False] * n
            children = [[] for _ in range(n)]

            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            
            q = deque([[0, -1, True]])

            while q:
                node, parent, isEven = q.popleft()
                evens[node] = isEven

                for child in children[node]:
                    if child == parent:
                        continue
                    q.append([child, node, not isEven])

            return evens 
        

        n1 = len(edges1)+1
        n2 = len(edges2)+1
        evens_1 = find_evens(edges1, n1)
        evens_2 = find_evens(edges2, n2)

        sum1 = sum(evens_1)
        sum2 = sum(evens_2)
        max_sum2 = max(n2 - sum2, sum2)

        return [max_sum2+(sum1 if even else n1-sum1) for even in evens_1]
        
print(Solution().maxTargetNodes(
    [[0,1],[0,2],[2,3],[2,4]],
    [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
))