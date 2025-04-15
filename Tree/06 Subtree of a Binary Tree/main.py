from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.isSametree(root1.left, root2.left) and self.isSametree(root1.right, root2.right)
        return False
tree1 = TreeNode(1)
tree1.right = TreeNode(3)
tree1.left = TreeNode(2)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.left.left.left = TreeNode(6)

tree2 = TreeNode(2)
tree2.left = TreeNode(4)
tree2.right = TreeNode(5)
tree2.left.left = TreeNode(6)

solution = Solution()
print(solution.isSubtree(tree1, tree2))
# Subtree of a Binary Tree
#
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The tree could also be considered as a subtree of itself.
#
# Example 1:
#
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
#
# Output: true
#
# Example 2:
#
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
#
# Output: false
#
# Constraints:
#
#     0 <= The number of nodes in both trees <= 100.
#     -100 <= root.val, subRoot.val <= 100
