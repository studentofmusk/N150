class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root: TrieNode):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)



wd = WordDictionary()
wd.addWord("Hello")
print(wd.search(".el.o"))


# Design Word Search Data Structure
#
# Design a data structure that supports adding new words and searching for existing words.
#
# Implement the WordDictionary class:
#
#     void addWord(word) Adds word to the data structure.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
# Example 1:
#
# Input:
# ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
#
# Output:
# [null, null, null, null, false, true, true, true]
#
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("day");
# wordDictionary.addWord("bay");
# wordDictionary.addWord("may");
# wordDictionary.search("say"); // return false
# wordDictionary.search("day"); // return true
# wordDictionary.search(".ay"); // return true
# wordDictionary.search("b.."); // return true
#
# Constraints:
#
#     1 <= word.length <= 20
#     word in addWord consists of lowercase English letters.
#     word in search consist of '.' or lowercase English letters.
#
