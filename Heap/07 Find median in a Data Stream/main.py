import heapq
import math
import random

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if (
                self.small and
                self.large and
                (-1 * self.small[0]) > self.large[0]
        ):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        return (-1 * self.small[0] + self.large[0]) / 2


#
# Find Median in a Data Stream
#
# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.
#
# For example:
#
#     For arr = [1,2,3], the median is 2.
#     For arr = [1,2], the median is (1 + 2) / 2 = 1.5
#
# Implement the MedianFinder class:
#
#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far.
#
# Example 1:
#
# Input:
# ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
#
# Output:
# [null, null, 1.0, null, 2.0, null, 2.0]
#
# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.findMedian(); // return 1.0
# medianFinder.addNum(3);    // arr = [1, 3]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(2);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
# Constraints:
#
#     -100,000 <= num <= 100,000
#     findMedian will only be called after adding at least one integer to the data structure.
#
