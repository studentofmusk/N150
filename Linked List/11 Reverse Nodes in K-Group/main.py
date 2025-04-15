from tokenize import group
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, curr = None, head
        head = main_tail = ListNode(0)
        i = 0
        while curr:
            tail = curr
            count = 0
            isEnd = False

            for i in range(k):
                if not curr:
                    isEnd = True
                    break

                count += 1
                # Reverse the node
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if isEnd:
                print("count:", count)
                curr, p = prev, None
                while count:
                    t = curr.next
                    curr.next = p
                    p = curr
                    curr = t
                    count -= 1

                main_tail.next = p
                break
            else:
                main_tail.next = prev
                main_tail = tail
                main_tail.next = None

        return head.next



    def given(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev= dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr:ListNode, k:int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

def create_LL(l: List[int]):
    head = ListNode(0)
    temp = head
    for val in l:
        temp.next = ListNode(val)
        temp = temp.next
    return head.next


def print_LL(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

solution = Solution()
p1 = create_LL([1,2,3,4,5,6])
print_LL(solution.reverseKGroup(p1, 4))
p1 = create_LL([1,2,3,4,5,6])
print_LL(solution.given(p1, 4))


# Reverse Nodes in K-Group
#
# You are given the head of a singly linked list head and a positive integer k.
#
# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.
#
# Return the modified list after reversing the nodes in each group of k.
#
# You are only allowed to modify the nodes' next pointers, not the values of the nodes.
#
# Example 1:
#
# Input: head = [1,2,3,4,5,6], k = 3
#
# Output: [3,2,1,6,5,4]
#
# Example 2:
#
# Input: head = [1,2,3,4,5], k = 3
#
# Output: [3,2,1,4,5]
#
# Constraints:
#
#     The length of the linked list is n.
#     1 <= k <= n <= 100
#     0 <= Node.val <= 100
#
