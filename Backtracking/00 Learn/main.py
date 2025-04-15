from typing import Optional, List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Backtracking:

    def canReachLeaf(self, root: Optional[TreeNode]):
        if not root or root.val == 0:
            return False
        if not root.right and not root.left:
            return True
        if self.canReachLeaf(root.left):
            return True
        if self.canReachLeaf(root.right):
            return True
        return False

    def leafPath(self, root: Optional[TreeNode], path:List[int] = []):

        if not root or root.val == 0:
            return False
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if self.leafPath(root.left, path):
            return True
        if self.leafPath(root.right, path):
            return True
        path.pop()
        return False


tree = TreeNode(4)
tree.left = TreeNode(0)
tree.left.right = TreeNode(7)
tree.right = TreeNode(1)
tree.right.left = TreeNode(2)
tree.right.right = TreeNode(0)

solution = Backtracking()
print(solution.canReachLeaf(tree))
print(solution.leafPath(tree))
