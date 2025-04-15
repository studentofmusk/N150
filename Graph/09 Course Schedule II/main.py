from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            adjList[src].append(dest)

        visiting = set()
        visited = set()
        result = []

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
            visiting.add(course)
            for neighbour in adjList[course]:
                if not dfs(neighbour):
                    return False

            visiting.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
             if not dfs(course):
                 return []

        return result[::-1]

print(Solution().findOrder(numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]))


# Course Schedule II
#
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
#
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
#
# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.
#
# Example 1:
#
# Input: numCourses = 3, prerequisites = [[1,0]]
#
# Output: [0,1,2]
#
# Explanation: We must ensure that course 0 is taken before course 1.
#
# Example 2:
#
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
#
# Output: []
#
# Explanation: It's impossible to finish all courses.
#
# Constraints:
#
#     1 <= numCourses <= 1000
#     0 <= prerequisites.length <= 1000
#     All prerequisite pairs are unique.
#
