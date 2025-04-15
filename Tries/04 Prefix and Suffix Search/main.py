# https://leetcode.com/problems/prefix-and-suffix-search/description/
from typing import List


class WordFilter:
    def __init__(self, words):
        self.prefix_suffix_map = {}

        # Preprocess all words
        for i, word in enumerate(words):
            n = len(word)
            # Iterate over all possible prefix lengths
            for prefix_len in range(n + 1):
                # Iterate over all possible suffix lengths
                for suffix_len in range(n + 1):
                    # Form the key using the prefix and suffix
                    prefix_suffix_key = word[:prefix_len] + '#' + word[-suffix_len:]
                    print(prefix_suffix_key)
                    self.prefix_suffix_map[prefix_suffix_key] = i

    def f(self, pref, suff):
        # Search for the combination of prefix and suffix in the map
        key = pref + '#' + suff
        return self.prefix_suffix_map.get(key, -1)


"""class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.index = -1
        self.length = 0

    def addWord(self, word: str, index: int) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.isWord = True
        curr.index = index
        curr.length = len(word)


class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i, w in enumerate(words):
            self.root.addWord(w, i)
        self.res = []

    def isPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return [False, None]
            curr = curr.children[c]
        return [True, curr]

    def isSuffix(self, suffix, node: TrieNode):
        if not(node.children):
            return

        curr = node

        for c in suffix:
            if c not in curr.children:
                for child in curr.children.values():
                    self.isSuffix(suffix, child)
                return
            curr = curr.children[c]

        if curr.isWord:
            if self.res:
                if self.res[1] < curr.length:
                    self.res = [curr.index, curr.length]
            else:
                self.res = [curr.index, curr.length]

    def f(self, pref: str, suff: str) -> int:
        l1 = self.isPrefix(pref)
        if l1[0]:
            if not suff:
                if l1[1].isWord:
                    return l1[1].index
                else: return -1
            if suff in pref:
                self.res = [l1[1].index, l1[1].length]
            else:
                self.res = []
            self.isSuffix(suff, l1[1])
            if self.res:
                return self.res[0]
            return -1
        return -1
"""

wf = WordFilter(words=["blue", "balloon", "battle", "b"])
# print(wf.isPrefix("battle"))

print(wf.f("ball", "loon"))

"""
#battle
#e
#le
#tle
#ttle
#attle
#battle
b#battle
"""