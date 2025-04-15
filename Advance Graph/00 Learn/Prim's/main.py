# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list of edges making up the minimum spanning tree.

import heapq
from typing import List

def minimumSpanningTree(edges: List[List[int]], n: int):

    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors.
    minHeap = []
    for neighbour, weight in adj[1]:
        heapq.heappush(minHeap, [weight, 1, neighbour])

    mst = []
    visit = set()
    visit.add(1)

    while len(visit) < n:
        weight, n1, n2 = heapq.heappop(minHeap)
        if n2 in visit:
            continue

        mst.append([n1, n2])
        visit.add(n2)
        for neighbour, weight in adj[n2]:
            if neighbour not in visit:
                heapq.heappush(minHeap, [weight, n2, neighbour])

    return mst
