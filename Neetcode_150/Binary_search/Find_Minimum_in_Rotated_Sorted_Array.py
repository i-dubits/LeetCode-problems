from typing import List
import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = -1
        r = len(nums)

        min_1 = math.inf
        min_2 = math.inf

        curr_min = min(nums[0], nums[-1])

        while l < r - 1:
            m = l + (r - l) // 2

            if nums[m] < curr_min:
                r = m
            else:
                l = m

        if l != -1:
            min_1 = nums[l]
        if r != len(nums):
            min_2 = nums[r]

        ans = min(min_1, min_2, curr_min)

        return ans




def full_pipeline(numbers):
    sol = Solution()
    ans = sol.findMin(numbers)
    # print(ans)
    return ans


numbers = [3,4,5,6,1,2]
print( full_pipeline(numbers) )


str_list = [
    [3,4,5,6,1,2],
    [4,5,0,1,2,3],
    [4,5,6,7],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )