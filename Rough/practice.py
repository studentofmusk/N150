from heapq import heapify, heappop

class UnionFind:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node:int)->int:
        
        res = node
        
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        
        return res 
    
    def union(self, n1:int, n2:int):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
class Kruskal_s:
    def mst(self, n: int, edges: list[list[int]]):
        
        union = UnionFind(n)
        minHeap = []

        for u, v, w in edges:
            minHeap.append((w, u, v))
        
        heapify(minHeap)

        mst: list[list[int]] = []

        while len(mst) < n-1:
            wei, n1, n2 = heappop(minHeap)

            if not union.union(n1, n2):
                continue
            mst.append([n1, n2])
        
        return mst


print(Kruskal_s().mst(
    n=5,
    edges=[
        [0, 1, 3],
        [1, 2, 2],
        [0, 2, 1],
        [2, 3, 4],
        [1, 4, 2],
        [4, 3, 1]
    ]
))

# Example Walkthrough

# Say we have a tree: 0 ← 1 ← 2 ← 3
# (i.e. parent[3]=2, parent[2]=1, parent[1]=0, parent[0]=0)

# find(3):

# res=3 → parent[3]=2 → not root

# compress: parent[3] = parent[2] = 1

# res=1 → parent[1]=0 → not root

# compress: parent[1] = parent[0] = 0

# res=0 → parent[0]=0 → stop

# Now parent array is [0,0,1,1]
# But after more finds, it will flatten further to [0,0,0,0].