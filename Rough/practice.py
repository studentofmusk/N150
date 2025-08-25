class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word:str):

        curr = self.root
        
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        
        curr.endOfWord = True
    
    def search(self, word:str):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.endOfWord


newTrie = Trie()
newTrie.insert("global")
newTrie.insert("mango")
print(newTrie.search("gta"))
print(newTrie.search("mango"))

