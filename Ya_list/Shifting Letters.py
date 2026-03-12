
from typing import List
from collections import defaultdict


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        inp_arr = [ord(ch) - ord('a') for ch in reversed(s)]

        shifts = list(reversed(shifts))
        pref_sum = [0] * len(shifts)
        pref_sum[0] = shifts[0]

        for i in range(1, len(shifts)):
            pref_sum[i] = pref_sum[i - 1] + shifts[i]

        res_arr = []
        for i in range(len(pref_sum)):
            new_numb = (inp_arr[i] + pref_sum[i]) % 26
            res_arr.append(chr(new_numb + ord('a')))

        ans = ''.join(reversed(res_arr))
        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.shiftingLetters(*nums)
    return ans

numbers = ["abc", [3,5,9]]
print( full_pipeline(numbers) )


str_list = [
    ["abc", [3,5,9]],
    ["aaa", [1,2,3]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )