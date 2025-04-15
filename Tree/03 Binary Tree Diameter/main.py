from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def print_tree(self)->None:
        if self.left:
            self.left.print_tree()
        print(self.val, end=" ")
        if self.right:
            self.right.print_tree()

class Solution:
    def __init__(self):
        self.res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dfs(root)
        return self.res

    def dfs(self, root: Optional[TreeNode])-> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left+right)
        return 1 + max(left, right)


    def given(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return res

solution = Solution()

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(4)
tree.right.left.left = TreeNode(5)
# tree.print_tree()
print("Practice:",solution.diameterOfBinaryTree(tree))
print("given:",solution.given(tree))

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(4)
tree.left.left = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.right.right = TreeNode(4)
tree.right.right.right.right = TreeNode(5)
print("Practice:",solution.diameterOfBinaryTree(tree))
print("given:",solution.given(tree))



# Binary Tree Diameter
#
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
#
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
#
# Given the root of a binary tree root, return the diameter of the tree.
#
# Example 1:
#
# Input: root = [1,null,2,3,4,5]
#
# Output: 3
#
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].
#
# Example 2:
#
# Input: root = [1,2,3]
#
# Output: 2
#
# Constraints:
#
#     1 <= number of nodes in the tree <= 100
#     -100 <= Node.val <= 100
#
