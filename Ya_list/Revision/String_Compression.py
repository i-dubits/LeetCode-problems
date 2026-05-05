
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ind = 0
        prev_ch = chars[0]
        prev_ch_freq = 1

        if len(chars) == 1:
            return 1

        for read_ind in range(1, len(chars)):
            curr_ch = chars[read_ind]
            if curr_ch == prev_ch:
                prev_ch = curr_ch
                prev_ch_freq += 1
            else:
                if prev_ch_freq == 1:
                    chars[write_ind] = prev_ch
                    write_ind += 1
                else:
                    str_to_write = prev_ch + str(prev_ch_freq)
                    for ind_in_str in range(len(str_to_write)):
                        chars[write_ind] = str_to_write[ind_in_str]
                        write_ind += 1
                prev_ch = curr_ch
                prev_ch_freq = 1

        if prev_ch_freq == 1:
            chars[write_ind] = prev_ch
            write_ind += 1
        else:
            str_to_write = prev_ch + str(prev_ch_freq)
            for ind_in_str in range(len(str_to_write)):
                chars[write_ind] = str_to_write[ind_in_str]
                write_ind += 1

        return write_ind

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
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )