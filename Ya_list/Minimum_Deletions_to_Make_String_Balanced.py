
from typing import List
from collections import defaultdict


class Solution:
    def minimumDeletions(self, source: str) -> int:
        source = [ord(el) - ord('a') for el in source]

        count_ones_left = [0]*len(source)
        curr_count_ones = 0
        for ind in range(1, len(source)):
            if source[ind - 1] == 1:
                curr_count_ones += 1
            count_ones_left[ind] = curr_count_ones

        count_zeros_right = [0]*len(source)
        curr_count_zeros = 0
        for ind in range(len(source) - 2, -1, -1):
            if source[ind + 1] == 0:
                curr_count_zeros += 1
            count_zeros_right[ind] = curr_count_zeros

        ans = len(source)
        for pair in zip(count_ones_left, count_zeros_right, strict=True):
            ans = min(ans, pair[0] + pair[1])

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.minimumDeletions(*nums)
    return ans

numbers = ["aababbab"]
print( full_pipeline(numbers) )


str_list = [
    ["aababbab"],
    ["bbaaaaabb"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )