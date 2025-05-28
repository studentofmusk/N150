from typing import List
from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def dfs(node, parent, children, k):
            if k < 0:
                return 0
            
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k - 1)
    
            return res
        

        def build(edges, k):
            n = len(edges)+1
            children = [[] for _ in range(n)]

            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)

            return res
        
        n = len(edges1) + 1
        count1 = build(edges1, k)
        count2 = build(edges2, k-1)
        maxCount2 = max(count2)

        res = [count1[i] + maxCount2 for i in range(n)]

        return res



print(Solution().maxTargetNodes(
    [[0,1],[0,2],[2,3],[2,4]],
    [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
    2
))