from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visiting = set()
        visited = set()

        for key, val in prerequisites:
            adjList[key].append(val)


        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            # Mark the current course as being processed
            visiting.add(course)

            # Process all the neighbours
            for neighbour in adjList[course]:
                if not dfs(neighbour):
                    return False

            # mark course as fully processed
            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


print(Solution().canFinish(numCourses=2, prerequisites=[[0, 1], [1, 0]]))
print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))

# Course Schedule
#
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
#
# The pair [0, 1], indicates that must take course 1 before taking course 0.
#
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
#
# Return true if it is possible to finish all courses, otherwise return false.
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[0,1]]
#
# Output: true
#
# Explanation: First take course 1 (no prerequisites) and then take course 0.
#
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
#
# Output: false
#
# Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.
#
# Constraints:
#
#     1 <= numCourses <= 1000
#     0 <= prerequisites.length <= 1000
#     All prerequisite pairs are unique.
#
