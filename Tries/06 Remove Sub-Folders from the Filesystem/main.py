from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path):

        node = self.root
        for folder in path.split("/")[1:]:
            if folder not in node.children:
                node.children[folder] = TrieNode()
            node = node.children[folder]

        node.endOfWord = True

    def search(self, path):

        node = self.root

        for folder in path.split("/")[1:]:
            if folder not in node.children:
                return False
            node = node.children[folder]
            if node.endOfWord:
                return True
        return False
                

class Solution:
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        res = []
        folder.sort()
        for path in folder:
            if not trie.search(path):
                trie.insert(path)
                res.append(path)
        return res

# Remove Sub-Folders from the Filesystem
# Solved 
# You are given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b".

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/neetcode" and "/neetcode/practice" are valid paths while an empty string "" and "/" are not.

# Example 1:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

# Example 2:

# Input: folder = ["/a","/a/b/c","/a/b/d"]

# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

# Example 3:

# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]

# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
# Constraints:

# 1 <= folder.length <= 40,000
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'.
# folder[i] always starts with the character '/'.
# Each folder name is unique.
