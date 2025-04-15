from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)

        return merged
    # --------------------------------------------------------------------------------
    def way1(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) > 1:
            intervals.sort(key=lambda x: x[0])
            res.append(intervals[0])
        else:
            return intervals


        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            elif res[-1][0] > intervals[i][1]:
                res += [intervals[i], res.pop()]
            else:
                end = res.pop()
                res.append([
                    min(end[0], intervals[i][0]),
                    max(end[1], intervals[i][1])
                ])
        return res

    # --------------------------------------------------------------------------------

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                new_interval = [
                    min(intervals[i][0], new_interval[0]),
                    max(intervals[i][1], new_interval[1])
                ]
        res.append(new_interval)
        return res

    def way2(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) > 1:
            res.append(intervals[0])
        else:
            return intervals

        for interval in intervals[1:]:
            res = self.insert(res, interval)

        return res

print(Solution().merge(intervals = [[1,3],[1,5],[6,7]]))
print(Solution().merge(intervals = [[1,2],[2,3]]))
# Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# You may return the answer in any order.
#
# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.
#
# Example 1:
#
# Input: intervals = [[1,3],[1,5],[6,7]]
#
# Output: [[1,5],[6,7]]
# Example 2:
#
# Input: intervals = [[1,2],[2,3]]
#
# Output: [[1,3]]
# Constraints:
#
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= start <= end <= 1000
