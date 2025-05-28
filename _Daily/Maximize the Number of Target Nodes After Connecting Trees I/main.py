from typing import List
from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        n = len(edges1)+1        
        m = len(edges2)+1        

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        max_cover_tree2 = 0
        if k-1 == 0:
            max_cover_tree2 = 1
        else:
            for node in range(m):
                max_cover_tree2 = max(self.bfs(adj2, node, k), max_cover_tree2)

        res = []
        for node in range(n):
            res.append(self.bfs(adj1, node, k+1)+max_cover_tree2)
        return res

    def bfs(self, adjList, node, level):

        q = deque([node])
        length = 0
        res = 0
        visit = set([node])

        while q and length < level:
            for _ in range(len(q)):
                node = q.popleft()
                res +=1
                for nei in adjList[node]:
                    if nei in visit:
                        continue
                    visit.add(nei)
                    q.append(nei)
            length += 1
        
        return res
        
print(Solution().maxTargetNodes(
    [[0,1],[0,2],[2,3],[2,4]],
    [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]],
    2
))