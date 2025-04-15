# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_list = ListNode()
        while head:
            new_list.val = head.val
            new_list = ListNode(0, new_list)
            head = head.next

        new_list = new_list.next
        return new_list


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.reverseList(head)

while new_head:
    print(new_head.val)
    new_head = new_head.next
    # Output: 5, 4, 3, 2, 1



# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

 
# Constraints:

#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

