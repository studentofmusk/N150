from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res = max(res, left + right + node.val)
            return node.val + max(left, right)

        dfs(root)
        return res


tree = TreeNode(-15)
tree.left = TreeNode(10)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(5)
tree.right.left.left = TreeNode(-5)
tree.right.left.right = TreeNode(-6)

solution = Solution()
print(solution.maxPathSum(tree))

# Binary Tree Maximum Path Sum
# Solved
#
# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Example 1:
#
# Input: root = [1,2,3]
#
# Output: 6
#
# Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.
#
# Example 2:
#
# Input: root = [-15,10,20,null,null,15,5,-5]
#
# Output: 40
#
# Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.
#
# Constraints:
#
#     -1000 <= Node.val <= 1000
#     1 <= The number of nodes in the tree <= 1000.

