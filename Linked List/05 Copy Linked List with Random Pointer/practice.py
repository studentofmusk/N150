from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]

solution = Solution()

head = [[1,None],[2,2],[3,2]]
LL = Node(1)
LL.next = Node(2)
LL.next.next = Node(3)
LL.next.random = LL.next.next
LL.next.next.random = LL.next.next

LL_copy = solution.copyRandomList(LL)



# Copy Linked List with Random Pointer

# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

#     The original value val of the copied node
#     A next pointer to the new node corresponding to the next pointer of the original node
#     A random pointer to the new node corresponding to the random pointer of the original node

# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: head = [[3,null],[7,3],[4,0],[5,1]]

# Output: [[3,null],[7,3],[4,0],[5,1]]

# Example 2:

# Input: head = [[1,null],[2,2],[3,2]]

# Output: [[1,null],[2,2],[3,2]]

# Constraints:

#     0 <= n <= 100
#     -100 <= Node.val <= 100
#     random is null or is pointing to some node in the linked list.

