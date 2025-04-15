from typing import Optional, List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow.next, None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            
def createLL(ele:List[int]):
    LL = ListNode(ele[0])
    temp = LL
    for val in ele[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return LL

def print_LL(curr:ListNode)-> None:
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

solution = Solution()



ele = [0, 1, 2, 3, 4, 5, 6]
LL1 = createLL(ele)
solution.reorderList(LL1)
print_LL(LL1) # output: 0 6 1 5 2 4 3

ele = [2,4,6,8]
LL1 = createLL(ele)
solution.reorderList(LL1)
print_LL(LL1) # output: 0 6 1 5 2 4 3


# Reorder Linked List

# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]

# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]

# Constraints:

#     1 <= Length of the list <= 1000.
#     1 <= Node.val <= 1000
