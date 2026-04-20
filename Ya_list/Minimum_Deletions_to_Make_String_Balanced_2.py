
from typing import List
from collections import defaultdict


class Solution:
    def minimumDeletions(self, source: str) -> int:
        my_stack = []

        cnt = 0
        for ind in range(len(source)):
            if source[ind] == 'a' and len(my_stack) != 0 and my_stack[-1] == 'b':
                cnt += 1
                my_stack.pop()
            else:
                my_stack.append(source[ind])

        return cnt

def full_pipeline(nums):

    sol = Solution()
    ans = sol.minimumDeletions(*nums)
    return ans

# numbers = ["aababbab"]
numbers = ["bbaaaaabb"]
print( full_pipeline(numbers) )


str_list = [
    ["aababbab"],
    ["bbaaaaabb"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )