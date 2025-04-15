from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        l = r = head
        isExist = False
        while r.next and i < n:
            r = r.next
            if i == n-1:
                isExist = True
                break
            i+=1
        if not isExist:
            return head.next
        
        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next

        prev.next = l.next       
        return head

        return r

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

# head = [1,2,3,4], n = 2
LL1 = createLL([1,2,3,4])
result1 = solution.removeNthFromEnd(head=LL1, n=2)
print_LL(result1)
# print(result1.val)

# head = [1,2,3,4], n = 2
LL2 = createLL([5])
result2 = solution.removeNthFromEnd(head=LL2, n=1)
print_LL(result2)



# Remove Node From End of Linked List

# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]

# Example 2:

# Input: head = [5], n = 1

# Output: []

# Example 3:

# Input: head = [1,2], n = 2

# Output: [2]

# Constraints:

#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz
