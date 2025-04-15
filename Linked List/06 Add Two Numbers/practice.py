""" Bravooooo! beats 93% of py developers speed """
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        rem = 0        
        while l1 and l2:
            
            Sum = l1.val + l2.val + rem
            rem = Sum//10
            dummy.next = ListNode(Sum % 10)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        bal = l1 or l2

        while bal:
            Sum = bal.val + rem
            rem = Sum//10
            dummy.next = ListNode(Sum%10)
            dummy = dummy.next
            bal = bal.next

        if rem:
            dummy.next = ListNode(rem)
        
        return res.next
        

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

LL1 = createLL([1,2,3])
LL2 = createLL([4,5,6])
# print_LL(LL1)
# print_LL(LL2)
result = solution.addTwoNumbers(LL1, LL2)
print_LL(result)

LL1 = createLL([9])
LL2 = createLL([9])
# print_LL(LL1)
# print_LL(LL2)
result = solution.addTwoNumbers(LL1, LL2)
print_LL(result)

LL1 = createLL([9, 9, 9, 9, 9])
LL2 = createLL([9, 9, 9, 9])
# print_LL(LL1)
# print_LL(LL2)
result = solution.addTwoNumbers(LL1, LL2)
print_LL(result)

# 9 9 9 9 9 9 9 
# 9 9 9 9 

# 3 4 5
# 3
# 40
# 500

# Add Two Numbers

# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:

# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.

# Example 2:

# Input: l1 = [9], l2 = [9]

# Output: [8,1]

# Constraints:

#     1 <= l1.length, l2.length <= 100.
#     0 <= Node.val <= 9
