# Given a connected graph represented by a list of edges, where
# edges[0] = src, edges[1] = dest, edges[2] = weight
# Find the shortest path from source to every other nodes in the graph.
# There are n nodes in the graph.
# O(E * logV) or O(E * logE)
# NOTE: V^2 = E

import heapq

def shortestPath(edges, n, src):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    # s -> src; d -> dest; w -> weight
    for s, d, w in edges:
        adj[s].append((d, w))

    shortest = {}
    minHeap = [(0, src)]
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for w2, n2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, (w1+w2, n2))
    return shortest

