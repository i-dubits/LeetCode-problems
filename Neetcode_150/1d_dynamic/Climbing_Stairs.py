
from collections import defaultdict
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

def full_pipeline(numbers):
    sol = Solution()
    ans = sol.climbStairs(*numbers)
    return ans


numbers = [2]
print( full_pipeline(numbers) )


str_list = [
    [2],
    [3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )