class Solution:

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        window = n-numFriends+1
        for i in range(n):
            res = max(res, word[i:min(i+window, n)])
        return res
    
    
    # TLE issue
    def answerString1(self, word: str, numFriends: int) -> str:
        
        res = set()
        def backtrack(word, stack, nums):
            if nums == 0:
                res.update(stack)
                return

            if not word:
                return
            
            ends = len(word)-nums+1

            for i in range(1, ends+1):
                stack.append(word[:i])
                backtrack(word[i:], stack, nums-1)
                stack.pop()
            return
        
        backtrack(word, [], numFriends)
        res = list(res)
        res.sort(reverse=True)
        return res[0]


print(Solution().answerString("dbca",2))
print(Solution().answerString("ebbbbc",2))
print(Solution().answerString("gggg",4))