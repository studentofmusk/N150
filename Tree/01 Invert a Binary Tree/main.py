from typing import Optional, List
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def create_tree(values: List[int]) -> TreeNode:
    root = TreeNode(values[0])
    for value in values[1:]:
        root.insert(value)
    return root

solution = Solution()
tree1 = create_tree([1,2,3,4,5,6,7])
tree1.print_tree()
print("\nresult:")
solution.invertTree(tree1).print_tree()

# Invert a Binary Tree
#
# You are given the root of a binary tree root. Invert the binary tree and return its root.
#
# Example 1:
#
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [1,3,2,7,6,5,4]
#
# Example 2:
#
# Input: root = [3,2,1]
#
# Output: [3,1,2]
#
# Example 3:
#
# Input: root = []
#
# Output: []
#
# Constraints:
#
#     0 <= The number of nodes in the tree <= 100.
#     -100 <= Node.val <= 100
