from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    
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


