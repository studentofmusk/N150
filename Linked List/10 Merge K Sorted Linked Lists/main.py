from heapq import merge
from logging.config import listen
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        temp = None
        for i in range(len(lists)):
            temp = self.merge(temp, lists[i])

        return temp

    def merge(self, l1: ListNode, l2: ListNode):
        head = ListNode(0)
        temp = head

        while l1 and l2:
            if l1.val > l2.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            else:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            temp = temp.next

        balance = l1 or l2
        if balance:
            temp.next = balance

        return head.next

    def given(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergeList.append(self.merge(l1, l2))
            lists = mergeList

        return lists[0]







def create_LL(l: List[int]):
    head = ListNode(0)
    temp = head
    for val in l:
        temp.next = ListNode(val)
        temp = temp.next
    return head.next

def prepare_args(lst: List[List[int]]):
    res = []
    for l in lst:
        res.append(create_LL(l))

    return res

def print_LL(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()



solution = Solution()

lists = [[1,2,4],[1,3,5],[3,6]]
# test merge function
# lst1 = prepare_args(lists)
# print_LL(solution.merge(lst1[0], lst1[1]))
lst1 = prepare_args(lists)
print_LL(solution.mergeKLists(lst1))
print_LL(solution.given(lst1))




# Merge K Sorted Linked Lists
#
# You are given an array of k linked list lists, where each list is sorted in ascending order.
#
# Return the sorted linked list that is the result of merging all the individual linked lists.
#
# Example 1:
#
# Input: lists = [[1,2,4],[1,3,5],[3,6]]
#
# Output: [1,1,2,3,3,4,5,6]
#
# Example 2:
#
# Input: lists = []
#
# Output: []
#
# Example 3:
#
# Input: lists = [[]]
#
# Output: []
#
# Constraints:
#
#     0 <= lists.length <= 1000
#     0 <= lists[i].length <= 100
#     -1000 <= lists[i][j] <= 1000
