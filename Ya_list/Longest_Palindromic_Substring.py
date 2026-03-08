from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.my_str = s
        self.str_len = len(s)

        ans = ''

        for ind in range(len(self.my_str)):
            curr_ans_odd = self.find_longest_pal_odd(ind)
            curr_ans_even = self.find_longest_pal_even(ind)

            if len(curr_ans_even) > len(curr_ans_odd):
                curr_ans = curr_ans_even
            else:
                curr_ans = curr_ans_odd

            if len(ans) < len(curr_ans):
                ans = curr_ans

        return ans

    def find_longest_pal_odd(self, ind):
        i = 1
        while (ind - i >= 0 and ind + i < self.str_len
               and self.my_str[ind - i] == self.my_str[ind + i]):
            i += 1

        if i == 1:
            return self.my_str[ind]
        else:
            return self.my_str[ind - i + 1: ind + i]

    def find_longest_pal_even(self, ind):
        i = 0
        while (ind - i >= 0 and ind + i + 1 < self.str_len
               and self.my_str[ind - i] == self.my_str[ind + i + 1]):
            i += 1
        if i == 0:
            return ""
        else:
            return self.my_str[ind - i + 1: ind + i + 1]


def full_pipeline(nums):

    sol = Solution()
    ans = sol.longestPalindrome(nums)
    return ans

numbers = "ababd"

print( full_pipeline(numbers) )


str_list = [
    "ababd",
    "abbc",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )