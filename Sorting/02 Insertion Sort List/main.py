from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 
        
        list_sorted = head
        head = head.next
        list_sorted.next = None

        while head:
            ptr = list_sorted
            prev =  None
            while ptr and head.val < ptr.val:
                prev = ptr
                ptr = ptr.next
            
            if not prev:
                temp = head.next
                head.next = list_sorted
                list_sorted = head
                head = temp
            
            else:
                temp = head.next
                prev.next = head
                head.next = ptr
                head = temp
                
        ptr = list_sorted
        res = None
        while ptr:
            temp = ptr.next
            ptr.next = res
            res = ptr
            ptr = temp
        return res