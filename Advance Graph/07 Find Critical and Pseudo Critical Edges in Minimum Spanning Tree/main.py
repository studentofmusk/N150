from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # [v1, v2, weight, index]

        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo_critical = [], []
        
        for n1, n2, e_w, i in edges:
        
            weights = 0
            uf = UnionFind(n)
            
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weights += w

            if max(uf.rank) != n or weights > mst_weight:
                critical.append(i)
                continue

            weights = e_w
            uf = UnionFind(n)
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weights += w

            if weights == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
        
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):

        while self.par[v1] != v1:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        elif self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
    
# Find Critical and Pseudo Critical Edges in Minimum Spanning Tree
# Solved 
# You are given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [a[i], b[i], weight[i]] represents a bidirectional and weighted edge between nodes a[i] and b[i]. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

# Example 1:

# Input: n = 4, edges = [[0,3,2],[0,2,5],[1,2,4]]

# Output: [[0,2,1],[]]
# Example 2:

# Input: n = 5, edges = [[0,3,2],[0,4,2],[1,3,2],[3,4,2],[2,3,1],[1,2,3],[0,1,1]]

# Output: [[4,6],[0,1,2,3]]
# Constraints:

# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= a[i] < b[i] < n
# 1 <= weight[i] <= 1000
# All pairs (a[i], b[i]) are distinct.