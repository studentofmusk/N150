from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = -float("inf")
        for start_i, end_i in intervals:
            if start_i < end:
                count += 1
            else:
                end = end_i
        return count

    def way1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 0
        prev = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < prev:
                prev = min(interval[1], prev)
                i+=1
            else:
                prev = interval[1]

        return i

print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,4],[1,4]]))
print(Solution().eraseOverlapIntervals(intervals = [[1,2],[2,4]]))
# Non-overlapping Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.
#
# Example 1:
#
# Input: intervals = [[1,2],[2,4],[1,4]]
#
# Output: 1
# Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.
#
# Example 2:
#
# Input: intervals = [[1,2],[2,4]]
#
# Output: 0
# Constraints:
#
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# -50000 <= start_i < end_i <= 50000