from typing import Optional, Deque, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, data):
        if self.val > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        elif self.val < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)
        else:
            self.val = data

    def print_tree(self)->None:
        if self.left:
            self.left.print_tree()
        print(self.val, end=" ")
        if self.right:
            self.right.print_tree()


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # DFS
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def BFS(self, root: Optional[TreeNode]) -> int: # BFS
        q: Deque[Optional[TreeNode]] = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

    def DFS_Iterative(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, dept = stack.pop()
            if node:
                res = max(res, dept)
                stack.append([node.left, dept+1])
                stack.append([node.right, dept+1])
        return res

def create_tree(values: List[int]) -> TreeNode:
    root = TreeNode(values[0])
    for value in values[1:]:
        root.insert(value)
    return root

solution = Solution()

l1 = create_tree([1, 2, 3, 4])
print(solution.maxDepth(l1)) # DFS solution
print(solution.BFS(l1)) # BFS solution
print(solution.DFS_Iterative(l1)) # DFS with iteration solution


# Depth of Binary Tree
#
# Given the root of a binary tree, return its depth.
#
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Example 1:
#
# Input: root = [1,2,3,null,null,4]
#
# Output: 3
#
# Example 2:
#
# Input: root = []
#
# Output: 0
#
# Constraints:
#
#     0 <= The number of nodes in the tree <= 100.
#     -100 <= Node.val <= 100
