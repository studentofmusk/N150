# Trie has O(n) or O(1) time complexity while insert and search
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("mango"))
print(trie.startsWith("ap"))


"""
Other way
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True

"""

# Implement Prefix Tree
# Solved
#
# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.
#
# Implement the PrefixTree class:
#
#     PrefixTree() Initializes the prefix tree object.
#     void insert(String word) Inserts the string word into the prefix tree.
#     boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
#     boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
# Example 1:
#
# Input:
# ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]
#
# Output:
# [null, null, true, false, true, null, true]
#
# Explanation:
# PrefixTree prefixTree = new PrefixTree();
# prefixTree.insert("dog");
# prefixTree.search("dog");    // return true
# prefixTree.search("do");     // return false
# prefixTree.startsWith("do"); // return true
# prefixTree.insert("do");
# prefixTree.search("do");     // return true
#
# Constraints:
#
#     1 <= word.length, prefix.length <= 1000
#     word and prefix are made up of lowercase English letters.
#
