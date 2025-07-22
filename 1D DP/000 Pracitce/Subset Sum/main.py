class Solution:
    @staticmethod
    def subsetsum(arr:list[int], target:int) -> bool:
        n = len(arr)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(n):
            for j in range(target, arr[i] - 1, -1):
                dp[j] = dp[j - arr[i]] or dp[j]

            if dp[target]:
                return True

        return dp[target]
    
print(Solution.subsetsum(
    arr=[1,2,5],
    target = 4
))