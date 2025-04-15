from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root

soltution = Solution()

Btree = soltution.buildTree(preorder = [1,2,3,4], inorder = [2,1,3,4])
Btree.print_tree()
# Binary Tree from Preorder and Inorder Traversal
#
# You are given two integer arrays preorder and inorder.
#
#     preorder is the preorder traversal of a binary tree
#     inorder is the inorder traversal of the same tree
#     Both arrays are of the same size and consist of unique values.
#
# Rebuild the binary tree from the preorder and inorder traversals and return its root.
#
# Example 1:
#
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
#
# Output: [1,2,3,null,null,null,4]
#
# Example 2:
#
# Input: preorder = [1], inorder = [1]
#
# Output: [1]
#
# Constraints:
#
#     1 <= inorder.length <= 1000.
#     inorder.length == preorder.length
#     -1000 <= preorder[i], inorder[i] <= 1000
#
