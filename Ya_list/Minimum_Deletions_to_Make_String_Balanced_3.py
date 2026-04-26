
from typing import List
from collections import defaultdict


class Solution:
    def minimumDeletions(self, source: str) -> int:
        dp = [0] * len(source)

        b_count_before_curr = 0
        if source[0] == 'b':
            b_count_before_curr += 1

        for ind in range(1, len(source)):
            if source[ind] == 'a':
                dp[ind] = min(dp[ind - 1] + 1, b_count_before_curr)
            else:
                dp[ind] = dp[ind - 1]
                b_count_before_curr += 1

        return dp[-1]

def full_pipeline(nums):

    sol = Solution()
    ans = sol.minimumDeletions(*nums)
    return ans

numbers = ["aababbab"]
# numbers = ["bbaaaaabb"]
print( full_pipeline(numbers) )


str_list = [
    ["aababbab"],
    ["bbaaaaabb"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )