from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -=1
            
            res = max(res, count)
        
        return res
    
    def withHeap(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

print(Solution().minMeetingRooms(
    intervals = [
        Interval(0, 40),
        Interval(5, 10),
        Interval(15, 20)
    ]
))

print(Solution().withHeap(
    intervals = [
        Interval(0, 40),
        Interval(5, 10),
        Interval(15, 20)
    ]
))

# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2