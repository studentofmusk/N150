# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, MAX: int) :
            left = right = curr = 0
            if root.val >= MAX:
                curr = 1
                MAX = root.val

            if root.left:
                left = dfs(root.left, MAX)
            if root.right:
                right = dfs(root.right, MAX)

            return curr + left + right

        if root:
            return dfs(root, root.val)
        return 0

    def given(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], MAX: int) -> int:
            if not node:
                return 0
            res = 1 if node.val >= MAX else 0
            MAX = max(node.val, MAX)

            res += dfs(node.right, MAX)
            res += dfs(node.left, MAX)

            return res
        return dfs(root, root.val)

solution = Solution()
tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(1)
tree.right.left = TreeNode(1)
tree.right.right = TreeNode(5)
tree.left.left = TreeNode(3)

print(solution.goodNodes(tree))

# Count Good Nodes in Binary Tree
#
# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
#
# Given the root of a binary tree root, return the number of good nodes within the tree.
#
# Example 1:
#
# Input: root = [2,1,1,3,null,1,5]
#
# Output: 3
#
# Example 2:
#
# Input: root = [1,2,-1,3,4]
#
# Output: 4
#
# Constraints:
#
#     1 <= number of nodes in the tree <= 100
#     -100 <= Node.val <= 100
