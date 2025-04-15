import collections
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)


        q = deque([beginWord])
        visit: set = {beginWord}
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            q.append(neiword)
                            visit.add(neiword)
            res += 1
        return 0

print(Solution().ladderLength(beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]))
print(Solution().ladderLength(beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]))
# Word Ladder
#
# You are given two words, beginWord and endWord, and also a list of words wordList. All the given words are of the same length, consisting of lowercase English letters, and are all distinct.
#
# Your goal is to transform beginWord into endWord by following the rules:
#
#     You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
#     You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
#
# Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.
#
# Example 1:
#
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
#
# Output: 4
#
# Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".
#
# Example 2:
#
# Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]
#
# Output: 0
#
# Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList.
#
# Constraints:
#
#     1 <= beginWord.length <= 10
#     1 <= wordList.length <= 100
