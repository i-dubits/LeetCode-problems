
from typing import List
from collections import defaultdict


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curr_vol = min(height[l], height[r]) * (r - l)
            ans = max(ans, curr_vol)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxArea(*nums)
    return ans

numbers = [[1,8,6,2,5,4,8,3,7]]

print( full_pipeline(numbers) )


str_list = [
    [[1,8,6,2,5,4,8,3,7]],
    [[1,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )