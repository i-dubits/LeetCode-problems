
from typing import List
from collections import defaultdict


class Solution:
    def decodeString(self, source: str) -> str:
        stack = [] # (previous_str: str, curr_str_repeat: int)
        curr_numb = 0
        curr_str = []

        for ind, curr_ch in enumerate(source):
            if curr_ch.isdecimal():
                curr_numb = curr_numb * 10 + int(curr_ch)

            elif curr_ch == '[':
                stack.append( (curr_str, curr_numb) )
                curr_str = []
                curr_numb = 0

            elif curr_ch == ']':
                prev_str, curr_repeat = stack.pop()

                repeated_curr = curr_str * curr_repeat
                prev_str.extend(repeated_curr)
                curr_str = prev_str

            elif curr_ch.isalpha():
                curr_str.append(curr_ch)

        return ''.join(curr_str)



def full_pipeline(nums):

    sol = Solution()
    ans = sol.decodeString(*nums)
    return ans


# numbers = ["3[a]2[bc]"]
numbers = ["3[a2[c]]"]
# numbers = ["2[2[yz]]"]
# numbers = ["3[z]2[2[y]pq4[2[jk]e1[f]]]ef"]
# numbers = ["10[leetcode]"]
print( full_pipeline(numbers) )


str_list = [
    ["3[a]2[bc]"],
    ["3[a2[c]]"],
    ["2[abc]3[cd]ef"],
    ["10[leetcode]"]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )