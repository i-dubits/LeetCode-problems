
from typing import List
from collections import defaultdict


class Solution:
    def validPalindrome(self, source: str) -> bool:
        l, r = self.check(source, 0, len(source) - 1)
        if l >= r:
            return True

        check_1_l, check_1_r = self.check(source, l+1, r)
        check_1 = check_1_l >= check_1_r
        check_2_l, check_2_r = self.check(source, l, r - 1)
        check_2 = check_2_l >= check_2_r

        return check_1 or check_2

    def check(self, source, l, r):
        while l < r:
            if source[l] == source[r]:
                l += 1
                r -= 1
            else:
                break

        return l, r



def full_pipeline(nums):

    sol = Solution()
    ans = sol.validPalindrome(*nums)
    return ans


# numbers = ["aba"]
numbers = ["deeee"]
print( full_pipeline(numbers) )


str_list = [
    ["aba"],
    ["abca"],
    ["abc"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )