from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dest in tickets}
        tickets.sort()

        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True

            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res

    def heirholzer_recursion(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]

print(Solution().findItinerary(tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]))


# Reconstruct Flight Path
# Solved
# You are given a list of flight tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.
#
# Each from_i and to_i consists of three uppercase English letters.
#
# Reconstruct the itinerary in order and return it.
#
# All the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.
#
# If there are multiple valid flight paths, return the lexicographically smallest one.
#
# For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
# You may assume all the tickets form at least one valid flight path.
#
# Example 1:
#
#
#
# Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
#
# Output: ["JFK","BUF","HOU","SEA"]
# Example 2:
#
#
#
# Input: tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
#
# Output: ["JFK","HOU","JFK","SEA","JFK"]
# Explanation: Another possible reconstruction is ["JFK","SEA","JFK","HOU","JFK"] but it is lexicographically larger.
#
# Constraints:
#
# 1 <= tickets.length <= 300
# from_i != to_i
