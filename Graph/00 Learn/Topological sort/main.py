# Given a directed a-cyclical graph, return a valid Topological ordering of the graph.
def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    for src, dest in edges:
        adj[src].append(dest)

    topSort = []
    visit = set()

    for i in range(1, n+1):
        dfs(i, adj, visit, topSort)

    topSort.reverse()
    return topSort

def dfs(src, adj, visit, topSort):
    if src in visit:
        return True

    visit.add(src)
    for nei in adj[src]:
        dfs(nei, adj, visit, topSort)

    topSort.append(src)