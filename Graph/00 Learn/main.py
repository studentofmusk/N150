# Matrix 2D Grid
from collections import deque
from itertools import count

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

# Count Paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if(
        min(r, c) < 0 or
        r == ROWS or
        c == COLS or
        (r, c) in visit or
        grid[r][c] == 1
    ):
        return 0

    if r == ROWS-1 and c == COLS-1:
        return 1
    visit.add((r, c))
    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)
    visit.remove((r, c))
    return count


print("Number of Possible paths:", dfs(grid, 0, 0, set()))


# shortest path from top left to bottom right
def bfs(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))
    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()

            if r == ROWS-1 and c == COLS-1:
                return length

            neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbours:
                if (
                    min(r+dr, c+dc) < 0 or
                    r+dr == ROWS or
                    c+dc == COLS or
                    (r+dr, c+dc) in visit or
                    grid[r+dr][c+dc] == 1
                ):
                    continue

                visit.add((r+dr, c+dc))
                queue.append((r+dr, c+dc))
        length += 1
    return length


print("Shortest path Length:", bfs(grid))



# Adjacency List

# Graph node used for adjacency List
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

# or use a HashMap
adjList = {"A":[], "B":[]}


# Create an adjacency List
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dest in edges:
    if src not in adjList:
        adjList[src] = []
    if dest not in adjList:
        adjList[dest] = []

    adjList[src].append(dest)

print(adjList)

# count routes
def dfs(node, target, visit, adjList):
    if node in visit:
        return 0
    if node == target:
        return 1

    visit.add(node)
    count = 0
    for neighbour in adjList[node]:
        count += dfs(neighbour, target, visit, adjList)
    visit.remove(node)

    return count


print("Number of path from ['A'] to ['E']:", dfs("A", "E", set(), adjList))

# Shortest path
def bfs(node, target, adjList):
    visit = set()
    queue = deque()
    visit.add(node)
    queue.append(node)
    length = 0

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node == target:
                return length


            for neighbour in adjList[node]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    queue.append(neighbour)
        length += 1

    return length

print("Shortest path length:", bfs("A", "E", adjList))

