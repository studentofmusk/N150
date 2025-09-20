# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
    
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def backtrack(node, target, stack):
            if not node:
                return False

            if node.val == target:
                stack.append(node)
                return True

            stack.append(node)
            if node.left and backtrack(node.left, target, stack):
                return True
            if node.right and backtrack(node.right, target, stack):
                return True
            stack.pop()
            return False

        p_a: list[TreeNode] = []
        q_a: list[TreeNode] = []

        backtrack(root, p.val, p_a)
        backtrack(root, q.val, q_a)
        
        res = root
        for a1, a2 in zip(p_a, q_a):
            if a1.val != a2.val:
                break
            res = a1

        return res

# Lowest Common Ancestor of a Binary Tree
# You are given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:



# Input: root = [5,3,4,2,1], p = 1, q = 2

# Output: 3
# Example 2:



# Input: root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12

# Output: 3
# Constraints:

# 2 <= The number of nodes in the tree <= 100,000.
# -1,000,000,000 <= Node.val <= 1,000,000,000
# All Node.val are unique.
# p != q
# p and q will both exist in the tree.