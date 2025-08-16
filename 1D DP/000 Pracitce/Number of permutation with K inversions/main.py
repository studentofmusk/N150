class Solution:
    def countPermWithkInversions(self, n: int, k:int) ->int:
        
        if n == 0:
            return 0
        
        if k == 0:
            return 1
        
        result = 0

        for i in range(min(k, n-1) + 1):
            result += self.countPermWithkInversions(n-1, k-i)
        return result


test_cases = [
    {"n":3, "k":1},
    {"n":3, "k": 3}
]

solution = Solution()

for test in test_cases:
    print(solution.countPermWithkInversions(**test))