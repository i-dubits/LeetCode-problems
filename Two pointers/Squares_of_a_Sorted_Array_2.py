
from typing import List
from collections import defaultdict

from prompt_toolkit.contrib.telnet import TelnetServer


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [None] * len(nums)
        ans_ind = len(nums) - 1

        while l <= r:
            first = nums[l]
            second = nums[r]

            if first**2 >= second**2:
                ans[ans_ind] = first**2
                l += 1
            else:
                ans[ans_ind] = second**2
                r -= 1
            ans_ind -= 1

        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.sortedSquares(*nums)
    return ans

numbers = [[-4,-1,0,3,10]]

print( full_pipeline(numbers) )


str_list = [
    [[-4,-1,0,3,10]],
    [[-7,-3,2,3,11]],
    [[-10000,-9999,-7,-5,0,0,10000]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )