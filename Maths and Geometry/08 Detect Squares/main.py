from typing import List
from collections import defaultdict
class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.ptsCount[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for y2 in self.ptsCount[x1]:
            side = y2 - y1
            if side == 0:
                continue

            x3, x4 = x1 + side, x1 - side
            res += (self.ptsCount[x1][y2] * self.ptsCount[x3][y1] *
                    self.ptsCount[x3][y2])

            res += (self.ptsCount[x1][y2] * self.ptsCount[x4][y1] *
                    self.ptsCount[x4][y2])
        return res

        
class CountSquares1:
    def __init__(self):
        self.points = []
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            if abs(py-y) != abs(px-x) or x == px or y == py:
                continue
            
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

        
            
solution = CountSquares()
solution.add([1, 1])
solution.add([2, 2])
solution.add([1, 2])
print(solution.count([2, 1]))


# Detect Squares
# You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

# Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
# Query - Given a single query point, count the number of ways to choose three additional points from the data structure such that the three points and the query point form a square. The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.
# Implement the CountSquares class:

# CountSquares() Initializes the object.
# void add(int[] point) Adds a new point point = [x, y].
# int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.
# Example 1:



# Input: 
# ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]
       
# Output:
# [null, null, null, null, 1, 0, null, 2]

# Explanation:
# CountSquares countSquares = new CountSquares();
# countSquares.add([1, 1]);
# countSquares.add([2, 2]);
# countSquares.add([1, 2]);

# countSquares.count([2, 1]);   // return 1.
# countSquares.count([3, 3]);   // return 0.
# countSquares.add([2, 2]);     // Duplicate points are allowed.
# countSquares.count([2, 1]);   // return 2. 
# Constraints:

# point.length == 2
# 0 <= x, y <= 1000
