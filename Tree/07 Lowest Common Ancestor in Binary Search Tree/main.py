from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        elif self.val < val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        else:
            self.val = val
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val, end=" ")
        if self.right:
            self.right.print_tree()

def create_tree(values: List[int]) -> TreeNode:
    root = TreeNode(values[0])
    for val in values[1:]:
        root.insert(val)
    return root

def print_flow(nodes: List[TreeNode]):
    for node in nodes:
        print(node.val, end=" ")

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.dfs(root, p, [])
        path_q = self.dfs(root, q, [])
        res = None
        if len(path_q) > len(path_p):
            itr = len(path_p)
        else:
            itr = len(path_q)

        for i in range(itr):
            if path_p[i].val == path_q[i].val:
                res = path_p[i]
            else:
                break
        return res

    def dfs(self, root: TreeNode, target:TreeNode, res: List[TreeNode]=[]):
        res.append(root)
        if target.val > root.val:
            return self.dfs(root.right, target, res)
        elif target.val < root.val:
            return self.dfs(root.left, target, res)
        else:
            return res

    def given(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

solution = Solution()
tree_1 = create_tree([3, 2, 4, 5, 6])
result = solution.lowestCommonAncestor(tree_1, TreeNode(6), TreeNode(2))
print_flow([result])
# Lowest Common Ancestor in Binary Search Tree
#
# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
#
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.
#
# Example 1:
#
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
#
# Output: 5
#
# Example 2:
#
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
#
# Output: 3
#
# Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.
#
# Constraints:
#
#     2 <= The number of nodes in the tree <= 100.
#     -100 <= Node.val <= 100
#     p != q
#     p and q will both exist in the BST.
