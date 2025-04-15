import heapq
from collections import deque, defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF]*(k+5) for _ in range(n)]

        for u, v, cost in flights:
            adj[u].append([v, cost])

        dist[src][0] = 0
        minHeap = [(0, src, -1)]  # cost, node, stops
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))

        return -1
    def bellmanFord(self, n: int, flights: List[List[int]], src: int ,dst: int, k: int) -> int:
        prices = [float("inf")]* n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < temp[d]:
                    temp[d] =  prices[s] + p

            prices = temp
        return -1 if prices[dst] == float("inf") else prices[dst]


    def bfs(self,n: int, flights: List[List[int]], src: int ,dst: int, k: int) -> int:
        # Create the adjacency list
        adj = defaultdict(list)
        for from_node, to_node, price in flights:
            adj[from_node].append((to_node, price))

        # BFS queue: (current_node, total_cost, stops)
        queue = deque([(src, 0, 0)])
        min_cost = {src: 0}

        while queue:
            node, cost, stops = queue.popleft()

            # If stops exceed the limit, skip
            if stops > k:
                continue

            for neighbor, price in adj[node]:
                new_cost = cost + price

                # Push to queue only if cheaper cost found or not visited within allowed stops
                if new_cost < min_cost.get(neighbor, float('inf')):
                    min_cost[neighbor] = new_cost
                    queue.append((neighbor, new_cost, stops + 1))

        return min_cost.get(dst, -1)

print(Solution().findCheapestPrice(
    n=4,
    flights=[[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]],
    src=0,
    dst=3,
    k=1
))
print(Solution().findCheapestPrice(
    n=10,
    flights = [[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10], [6, 8, 6], [7, 9, 4], [1, 5, 4],
           [1, 0, 4], [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6], [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5],
           [5, 2, 4], [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]],
    src = 6,
    dst = 0,
    k = 7
))
print(Solution().findCheapestPrice(
    n=3,
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
    src = 0,
    dst = 2,
    k = 1
))

# Cheapest Flights Within K Stops
# There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.
#
# You are also given three integers src, dst, and k where:
#
# src is the starting airport
# dst is the destination airport
# src != dst
# k is the maximum number of stops you can make (not including src and dst)
# Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.
#
# Example 1:
#
#
#
# Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1
#
# Output: 500
# Explanation:
# The optimal path with at most 1 stop from airport 0 to 3 is shown in red, with total cost 200 + 300 = 500.
# Note that the path [0 -> 1 -> 2 -> 3] costs only 400, and thus is cheaper, but it requires 2 stops, which is more than k.
#
# Example 2:
#
#
#
# Input: n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1
#
# Output: 200
# Explanation:
# The optimal path with at most 1 stop from airport 1 to 2 is shown in red and has cost 200.
#
# Constraints:
#
# 1 <= n <= 100
# fromi != toi
# 1 <= pricei <= 1000
# 0 <= src, dst, k < n