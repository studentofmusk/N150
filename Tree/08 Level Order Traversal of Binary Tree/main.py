from typing import List, Optional, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q:Deque[TreeNode] = deque()
        if root:
            q.append(root)
        res = []
        while q:
            each = []
            for i in range(len(q)):
                node = q.popleft()
                each.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(each)
        return res

tree = TreeNode(4)
tree.right = TreeNode(3)
tree.left = TreeNode(5)
tree.right.left = TreeNode(9)

solution = Solution()
print(solution.levelOrder(tree))
# Level Order Traversal of Binary Tree
#
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
#
# Example 1:
#
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [[1],[2,3],[4,5,6,7]]
#
# Example 2:
#
# Input: root = [1]
#
# Output: [[1]]
#
# Example 3:
#
# Input: root = []
#
# Output: []
#
# Constraints:
#
#     0 <= The number of nodes in both trees <= 1000.
#     -1000 <= Node.val <= 1000
