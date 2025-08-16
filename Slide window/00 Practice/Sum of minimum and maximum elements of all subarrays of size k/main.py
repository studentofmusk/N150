class Solution:

    def subSumOfK(self, arr: list[int], k: int):
        pass
    
    def brute(self, arr: list[int], k: int):
        n = len(arr)
        res = 0
        for i in range(0, n-k+1):
            Min = Max = arr[i]
            for j in range(i, i+k):
                Min = min(arr[j], Min)
                Max = max(arr[j], Max)
            res += (Min + Max)
        return res


solution = Solution()
print(solution.subSumOfK([2, 5, -1, 7, -3, -1, -2], 4))