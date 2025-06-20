from typing import List
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        overlay_arr = [0]*(2*limit+2)
        
        for i in range(n//2):
            left_boundary = min(nums[i], nums[n-i-1])+1
            no_move_value = nums[i] + nums[n-i-1]
            right_boundary = max(nums[i], nums[n-i-1]) + limit

            overlay_arr[left_boundary] -= 1
            overlay_arr[no_move_value] -= 1
            overlay_arr[no_move_value+1] += 1
            overlay_arr[right_boundary+1] += 1
        curr_move = n
        res = float("inf")
        for i in range(2, 2*limit+1):
            curr_move += overlay_arr[i]
            res = min(res, curr_move)

        return res
        
print(Solution().minMoves(nums = [1,2,4,3], limit = 4))