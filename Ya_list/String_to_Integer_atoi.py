from typing import List


class Solution:
    def myAtoi(self, my_str: str) -> int:

        ans = []
        is_pos = True
        expect_leading_zero = True

        ptr = 0
        my_str = my_str.strip()
        if len(my_str) == 0:
            return 0
        first = my_str[ptr]
        if first == "-":
            is_pos = False
            ptr += 1
            ans.append("-")
        elif first == "+":
            is_pos = True
            ptr += 1

        while ptr < len(my_str):
            if ord('0') <= ord(my_str[ptr]) <= ord('9'):
                if ord(my_str[ptr]) == ord('0'):
                    if expect_leading_zero:
                        pass
                    else:
                        ans.append(my_str[ptr])
                else:
                    ans.append(my_str[ptr])
                    expect_leading_zero = False
                ptr += 1
            else:
                break

        if len(ans) == 0:
            ans_int = 0
        elif len(ans) == 1 and ans[0] == '-' or ans[0] == '+':
            ans_int = 0
        else:
            ans_int = int(''.join(ans))

        if ans_int < -2**31:
            ans_int = -2**31

        if ans_int > 2**31 - 1:
            ans_int = 2**31 - 1

        return ans_int

def full_pipeline(nums):

    sol = Solution()
    ans = sol.myAtoi(nums)
    return ans

# numbers = "42"
numbers = "0-1"

print( full_pipeline(numbers) )


str_list = [
    "42",
    " -042",
    "1337c0d3",
    "0-1",
    "words and 987",
    "-+12",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )