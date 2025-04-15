from typing import List
#----------- GO through Union Find Algo ------------
class Solution:
    def usingUnion(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res


        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        count = 0
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)

            return

        for node in range(n):
            if node in visit: continue
            count += 1
            dfs(node)

        return count


n=3
edges=[[0,1], [0,2]]

print(Solution().usingUnion(n, edges))
# print(Solution().countComponents(n, edges))
#
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
# print(Solution().countComponents(n, edges))
# Count Connected Components
#
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
#
# The nodes are numbered from 0 to n - 1.
#
# Return the total number of connected components in that graph.
#
# Example 1:
#
# Input:
# n=3
# edges=[[0,1], [0,2]]
#
# Output:
# 1
#
# Example 2:
#
# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]
#
# Output:
# 2
#
# Constraints:
#
#     1 <= n <= 100
#     0 <= edges.length <= n * (n - 1) / 2
#
