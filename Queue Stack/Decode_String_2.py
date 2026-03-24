
from typing import List
from collections import defaultdict


class Solution:
    def decodeString(self, source: str) -> str:
        stack_numb = []
        stack_str = []
        ans = []
        curr = ''
        curr_numb = 1

        ind = 0
        while ind < len(source):
            if len(stack_numb) == 0:
                ans.append(curr)
                curr = ''

            if source[ind].isnumeric():
                ind, curr_numb = self.read_numb(source, ind)

            elif source[ind] == '[':
                stack_numb.append(curr_numb)
                stack_str.append(curr)
                curr = ''
                ind += 1

            elif source[ind].isalpha():
                ind, word = self.read_word(source, ind)
                if len(stack_numb) == 0:
                    ans.append(word)
                else:
                    curr += word

            elif source[ind] == ']':
                prev_word = stack_str.pop()
                curr_numb = stack_numb.pop()

                curr = curr * curr_numb
                curr = prev_word + curr
                ind += 1

            else:
                print('something unexpected')

        ans.append(curr)
        return ''.join(ans)

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