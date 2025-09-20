from typing import List, Optional
from collections import deque, defaultdict 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        idToArray = defaultdict(list)

        q = deque([(root, 0)])

        while q:
            for _ in range(len(q)):
                
                node, groupId = q.popleft()
                
                idToArray[groupId].append(node.val)

                if node.left:
                    q.append((node.left, groupId-1))
                if node.right:
                    q.append((node.right, groupId+1))
        
        
        return [idToArray[key] for key in sorted(idToArray)]


# Binary Tree Vertical Order Traversal

# You are given the root node of a binary tree, return the vertical order traversal of its nodes' values.

# For the vertical order traversal, list the nodes column by column starting from the leftmost column and moving to the right.

# Within each column, the nodes should be listed in the order they appear from the top of the tree to the bottom.

# If two nodes are located at the same row and column, the node that appears to the left should come before the other.

# Example 1:



# Input: root = [1,2,3,4,5,6,7]

# Output: [[4],[2],[1,5,6],[3],[7]]
# Example 2:



# Input: root = [1,2,3,null,4,5,null]

# Output: [[2],[1,4,5],[3]]
# Constraints:

# 0 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100
