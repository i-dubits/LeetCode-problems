
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = len(nums) + 1

        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while l <= r and curr_sum >= target:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len

def full_pipeline(nums):

    sol = Solution()
    ans = sol.minSubArrayLen(*nums)
    return ans

# numbers = [10, [2,1,5,1,5,3]]
numbers = [4, [1,4,4]]

print( full_pipeline(numbers) )


str_list = [
    [10, [2,1,5,1,5,3]],
    [5, [1,2,1]],
    [7, [2,3,1,2,4,3]],
    [4, [1,4,4]],
    [11, [1,1,1,1,1,1,1,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )