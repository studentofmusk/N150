# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(10)
l1.next.next.next.next = ListNode(10)


l2 = ListNode(1)
l2.next = ListNode(4)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(10)
l2.next.next.next.next = ListNode(11)
solution = Solution()
result = solution.mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next


# Merge Two Sorted Linked Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]

# Example 3:

# Input: list1 = [], list2 = []

# Output: []

# Constraints:

#     0 <= The length of the each list <= 100.
#     -100 <= Node.val <= 100
