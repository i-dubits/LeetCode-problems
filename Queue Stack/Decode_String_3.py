
from typing import List
from collections import defaultdict


class Solution:
    def decodeString(self, source: str) -> str:
        stack_numb = []
        stack_str = []
        curr = ''

        curr_ind = 0
        while curr_ind < len(source):
            if source[curr_ind].isnumeric():
                curr_ind, numb = self.read_numb(source, curr_ind)
                stack_numb.append(numb)

                stack_str.append(curr)
                curr = ''
                curr_ind += 1

            elif source[curr_ind].isalpha():
                curr_ind, word = self.read_word(source, curr_ind)
                if len(curr) == 0:
                    curr = word
                else:
                    curr = curr + word

            elif source[curr_ind] == ']':
                if stack_numb:
                    multiplier = stack_numb.pop()
                else:
                    multiplier = 1
                if stack_str:
                    prev_word = stack_str.pop()
                else:
                    prev_word = ''

                curr = prev_word + curr * multiplier

                curr_ind += 1

            else:
                print('unexpected situation')

        return curr


    def read_numb(self, source:str, start_ind: int):
        numb_list = []
        ind = start_ind
        while ind < len(source) and source[ind].isnumeric():
            numb_list.append(source[ind])
            ind += 1
        return ind, int(''.join(numb_list))

    def read_word(self, source: str, start_ind: int):
        char_list = []
        ind = start_ind
        while (ind < len(source)
               and not source[ind].isnumeric() and source[ind] != ']'
               and source[ind] != '['):
            char_list.append(source[ind])
            ind += 1
        return ind, ''.join(char_list)


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