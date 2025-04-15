from collections import deque
from typing import Optional, List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # It'll only return right side nodes : drawback
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, res=[]):
            if not root:
                return res
            res.append(root.val)
            if not root.right:
                return res
            else:
                return dfs(root.right, res)

        return dfs(root)

    def given(self, root: Optional[TreeNode]) -> List[int]:
        q: Deque[TreeNode] = deque([root])
        res = []
        while q:
            rightNode = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(rightNode.left)
                    q.append(rightNode.right)
            if rightNode:
                res.append(rightNode.val)
        return res
tree = TreeNode(1)
tree.right = TreeNode(2)
solution = Solution()
print(solution.rightSideView(tree))
#Binary Tree Right Side View
#
# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
#
# Example 1:
#
# Input: root = [1,2,3]
#
# Output: [1,3]
#
# Example 2:
#
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [1,3,7]
#
# Constraints:
#
#     0 <= number of nodes in the tree <= 100
#     -100 <= Node.val <= 100
#
