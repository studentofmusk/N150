from typing import Optional, List


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

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def given(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False




def create_tree(values: List[int]):
    root = TreeNode(values[0])
    for val in values[1:]:
        root.insert(val)
    return root
# Same trees
tree1 = create_tree([1, 2, 3, 4])
tree2 = create_tree([1, 2, 3, 4])

solution = Solution()
print(solution.isSameTree(tree1, tree2))



# Same Binary Tree
#
# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
#
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
#
# Example 1:
#
# Input: p = [1,2,3], q = [1,2,3]
#
# Output: true
#
# Example 2:
#
# Input: p = [4,7], q = [4,null,7]
#
# Output: false
#
# Example 3:
#
# Input: p = [1,2,3], q = [1,3,2]
#
# Output: false
#
# Constraints:
#
#     0 <= The number of nodes in both trees <= 100.
#     -100 <= Node.val <= 100
