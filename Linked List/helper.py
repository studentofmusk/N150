from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

