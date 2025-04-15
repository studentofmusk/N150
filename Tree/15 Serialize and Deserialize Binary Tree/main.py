from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()


def print_Tree(node):
    if node.left:
        print_Tree(node.left)
    print(node.val, end=" ")
    if node.right:
        print_Tree(node.right)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(6)
tree.right.left.left = TreeNode(7)
tree.right.left.right = TreeNode(8)
tree.right.right.right = TreeNode(9)

codec = Codec()
print("Original:")
print_Tree(tree)
serial = codec.serialize(tree)
print("\n"+serial)
print_Tree(codec.deserialize(serial))
# Serialize and Deserialize Binary Tree
#
# Implement an algorithm to serialize and deserialize a binary tree.
#
# Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.
#
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.
#
# Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.
#
# Example 1:
#
# Input: root = [1,2,3,null,null,4,5]
#
# Output: [1,2,3,null,null,4,5]
#
# Example 2:
#
# Input: root = []
#
# Output: []
#
# Constraints:
#
#     0 <= The number of nodes in the tree <= 1000.
#     -1000 <= Node.val <= 1000
#
