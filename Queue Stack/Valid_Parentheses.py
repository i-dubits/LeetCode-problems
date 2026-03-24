
from typing import List
from collections import defaultdict


class Solution:
    def isValid(self, source: str) -> bool:
        valid_open = {']':'[', ')':'(', '}':'{'}
        my_stack = []

        ans = True
        for curr_ch in source:
            if curr_ch in ['(', '{', '[']:
                my_stack.append(curr_ch)
            elif curr_ch in [')', '}', ']']:
                if len(my_stack) != 0:
                    cand = my_stack.pop()
                    if cand != valid_open[curr_ch]:
                        ans = False
                        break
                else:
                    ans = False
                    break
            else:
                print(f'ERROR: invalid input')

        if len(my_stack) != 0:
            ans = False
        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.isValid(*nums)
    return ans


numbers = ["()"]
print( full_pipeline(numbers) )


str_list = [
    ["()"],
    ["()[]{}"],
    ["(]"],
    [""]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )