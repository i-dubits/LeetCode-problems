
from typing import List
from collections import defaultdict


class Solution:
    def compress(self, chars: List[str]) -> int:
        total_length = 0
        l = 0

        if len(chars) == 1:
            return 1

        curr_ch = chars[0]
        curr_ch_count = 1
        for r in range(1, len(chars)):
            if chars[r] == curr_ch:
                curr_ch_count += 1
            else:
                if curr_ch_count == 1:
                    chars[l] = curr_ch
                    total_length += 1
                    l += 1
                else:
                    to_write = curr_ch + str(curr_ch_count)
                    for symbol in to_write:
                        chars[l] = symbol
                        l += 1
                    total_length += len(to_write)

                curr_ch_count = 1
                curr_ch = chars[r]


        if curr_ch_count == 1:
            chars[l] = curr_ch
            total_length += 1
        else:
            to_write = curr_ch + str(curr_ch_count)
            for symbol in to_write:
                chars[l] = symbol
                l += 1
            total_length += len(to_write)

        return total_length



def full_pipeline(nums):

    sol = Solution()
    ans = sol.compress(*nums)
    return ans

numbers = [["a","a","b","b","c","c","c"]]
print( full_pipeline(numbers) )


str_list = [
    [["a","a","b","b","c","c","c"]],
    [["a"]],
    [["a","b","b","b","b","b","b","b","b","b","b","b","b"]],
    [["a","a","a","b","b","a","a"]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )