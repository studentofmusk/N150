from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            p = par[n]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

edges = [[1,2],[1,3],[3,4],[2,4]]
print(Solution().findRedundantConnection(edges))
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
print(Solution().findRedundantConnection(edges))
edges = [[6,13],[15,22],[10,13],[12,24],[3,23],[19,20],[3,12],[2,16],[19,23],[2,11],[18,23],[1,25],[2,17],[4,5],[14,19],[2,3],[1,7],[4,6],[9,10],[8,22],[7,22],[13,18],[13,21],[15,23],[5,25]]
print(Solution().findRedundantConnection(edges))

# Redundant Connection
# 
# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.
# 
# We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.
# 
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.
# 
# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.
# 
# Example 1:
# 
# Input: edges = [[1,2],[1,3],[3,4],[2,4]]
# 
# Output: [2,4]
# 
# Example 2:
# 
# Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
# 
# Output: [3,4]
# 
# Constraints:
# 
#     n == edges.length
#     3 <= n <= 100
#     1 <= edges[i][0] < edges[i][1] <= edges.length
#     There are no repeated edges and no self-loops in the input.
# 
