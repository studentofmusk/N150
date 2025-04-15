from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        each = set()
        while curr:
            if curr in each:
                return True
            each.add(curr)
            curr = curr.next
        return False

    def given(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


def createLL(ele:List[int]) -> ListNode:
    from random import choice
    nodes = []
    LL:ListNode = ListNode(ele[0])

    temp = LL
    for val in ele[1:]:
        temp.next = ListNode(val)
        nodes.append(temp.next)
        temp = temp.next

    temp.next = choice(nodes[:-1])
    return LL

def print_LL(curr:ListNode)-> None:
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

solution = Solution()

LL1 = createLL([1,2,3])
# print_LL(LL1)
print(solution.hasCycle(LL1))



# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.

# Example 1:

# Input: head = [1,2,3,4], index = 1

# Output: true

# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:

# Input: head = [1,2], index = -1

# Output: false

# Constraints:

#     1 <= Length of the list <= 1000.
#     -1000 <= Node.val <= 1000
#     index is -1 or a valid index in the linked list.

