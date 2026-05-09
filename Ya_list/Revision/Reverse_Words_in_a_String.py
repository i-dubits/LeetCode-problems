
from typing import List


class Solution:
    def reverseWords(self, source: str) -> str:
        source = list(source)

        last_str_ind = self.remove_extr_spaces(source)
        self.reverse_list(source, 0, last_str_ind)

        word_start = 0
        for ind in range(0, last_str_ind + 1):
            if source[ind] == ' ':
                word_end = ind - 1
                self.reverse_list(source, word_start, word_end)
                word_start = ind + 1

        self.reverse_list(source, word_start, last_str_ind)
        return ''.join(source[:last_str_ind+1])

    def reverse_list(self, source: list, first_ind: int, last_ind: int):
        while first_ind < last_ind:
            source[first_ind], source[last_ind] = source[last_ind], source[first_ind]
            first_ind += 1
            last_ind -= 1

    def remove_extr_spaces(self, source:list):
        write_ind = 0

        prev_char = None

        read_ind = 0 if source[0] != " " else 1
        for read_ind in range(read_ind, len(source)):
            curr_ch = source[read_ind]
            if curr_ch == ' ':
                if prev_char is None:
                    continue
                else:
                    if prev_char == ' ':
                        continue
                    else:
                        source[write_ind] = source[read_ind]
                        write_ind += 1
                        prev_char = curr_ch

            else:
                prev_char = curr_ch
                source[write_ind] = source[read_ind]
                write_ind += 1

        last_str_ind = write_ind - 1
        while source[last_str_ind] == ' ':
            last_str_ind -= 1
        return last_str_ind

def full_pipeline(nums):

    sol = Solution()
    ans = sol.reverseWords(*nums)
    return ans

# numbers = ["the sky is blue"]
numbers = ["  hello world  "]

print( full_pipeline(numbers) )


str_list = [
    ["the sky is blue"],
    ["  hello world  "],
    ["a good   example"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )