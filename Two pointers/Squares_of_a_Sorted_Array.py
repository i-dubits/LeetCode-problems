
from typing import List
from collections import defaultdict

from prompt_toolkit.contrib.telnet import TelnetServer


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first_non_neg_ind = len(nums)
        last_neg_ind = -1
        ans = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                first_non_neg_ind = i
                break

        last_neg_ind = first_non_neg_ind - 1
        while first_non_neg_ind < len(nums) or last_neg_ind > -1:
            if first_non_neg_ind < len(nums) and last_neg_ind > -1:
                first_val = abs(nums[first_non_neg_ind])
                second_val = abs(nums[last_neg_ind])

                if first_val <= second_val:
                    ans.append(first_val**2)
                    first_non_neg_ind += 1
                else:
                    ans.append(second_val**2)
                    last_neg_ind -= 1

            elif first_non_neg_ind >= len(nums):
                first_val = abs(nums[last_neg_ind])
                ans.append(first_val**2)
                last_neg_ind -= 1

            elif last_neg_ind <= -1:
                first_val = nums[first_non_neg_ind]
                ans.append(first_val**2)
                first_non_neg_ind += 1

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