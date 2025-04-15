from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for n in nums:
            if n in h:
                return True
            h.add(n)
        return False

solution = Solution()
print(solution.hasDuplicate([2, 4, 5, 6, 3]))
print(solution.hasDuplicate([2, 4, 5, 5, 3]))