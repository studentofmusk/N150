from functools import lru_cache
class Solution:
    @staticmethod
    def minJump(arr: list[int]):
        n = len(arr)
        dp = [float("inf")] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, min(i+arr[i]+1, n)):
                if dp[j] != float("inf"):
                    dp[i] = min(dp[i], dp[j]+1)
                    
        if dp[0] == float('inf'):
            return -1
        else: return dp[0]

    @staticmethod
    def memo(arr: list[int]):
        n = len(arr)
        cache: dict[int, int] = {}
        def dfs(index):
            if index >= n-1:
                return 0
            
            if index in cache:
                return cache[index]
            
            if arr[index] == 0:
                return -1
            
            max_jump = arr[index] + index
            res = float("inf")

            for i in range(index+1, max_jump+1):
                hand = dfs(i)
                if hand != -1:
                    res = min(1 + hand, res)

            cache[index] = res if res != float("inf") else -1
            return cache[index]
        return dfs(0)
    
    @staticmethod
    def brute(arr: list[int]):
        n = len(arr)
        def dfs(index):
            if index >= n-1:
                return 0
            if arr[index] == 0:
                return -1
            
            max_jump = arr[index] + index
            res = float("inf")

            for i in range(index+1, max_jump+1):
                hand = dfs(i)
                if hand != -1:
                    res = min(1 + hand, res)

            return res if res != float("inf") else -1
        return dfs(0)
    

test_case = [
    {"arr": [1, 4, 3, 2, 6, 7]},
    {"arr":[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]},
    {"arr": [0, 10, 20]}
]

for test in test_case:
    print("-"* 10)
    print(Solution.minJump(**test))
    print(Solution.memo(**test))
    print(Solution.brute(**test))