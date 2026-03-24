
from typing import List
from collections import defaultdict


class Solution:
    def decodeString(self, source: str) -> str:
        ans = []
        stack :int = []

        for i in range(len(source)):
            if source[i] != ']':
                stack.append(source[i])

            else:
                curr_str_str = ''
                while stack and stack[-1] != '[':
                    curr_str_str = stack.pop() + curr_str_str
                stack.pop()

                curr_numb_str = ''
                while stack and stack[-1].isnumeric():
                    curr_numb_str = stack.pop() + curr_numb_str
                curr_numb_int = int(curr_numb_str)

                str_to_add = curr_str_str * curr_numb_int

                if not stack:
                    ans.append(str_to_add)
                else:
                    stack.append(str_to_add)


        return ''.join(ans) + ''.join(stack)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.decodeString(*nums)
    return ans


# numbers = ["3[a]2[bc]"]
numbers = ["10[leetcode]"]
print( full_pipeline(numbers) )


str_list = [
    ["3[a]2[bc]"],
    ["3[a2[c]]"],
    ["2[abc]3[cd]ef"],
    ["10[leetcode]"]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )