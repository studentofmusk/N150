from typing import Optional, List
from unittest.mock import right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n+=1
            if n == k:
                return curr.val

            curr = curr.right



Btree = TreeNode(4)
Btree.left = TreeNode(3)
Btree.right = TreeNode(5)
Btree.left.left = TreeNode(2)


solution = Solution()
print(solution.kthSmallest(Btree, 4))

# Kth Smallest Integer in BST
#
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
#
# A binary search tree satisfies the following constraints:
#
#     The left subtree of every node contains only nodes with keys less than the node's key.
#     The right subtree of every node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees are also binary search trees.
#
# Example 1:
#
# Input: root = [2,1,3], k = 1
#
# Output: 1
#
# Example 2:
#
# Input: root = [4,3,5,2,null], k = 4
#
# Output: 5
#
# Constraints:
#
#     1 <= k <= The number of nodes in the tree <= 1000.
#     0 <= Node.val <= 1000
