from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # check if its the start of a sequence
            if (num -1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

solution = Solution()
print(solution.longestConsecutive([2,20,4,10,3,4,5]))
print(solution.longestConsecutive([0,3,2,5,4,6,1,1]))
print(solution.longestConsecutive([0,-1]))
