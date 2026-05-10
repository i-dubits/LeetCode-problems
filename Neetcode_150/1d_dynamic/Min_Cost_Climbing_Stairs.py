
from collections import defaultdict
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            if i == len(cost):
                ans = min(dp[i - 1], dp[i - 2])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return ans


def full_pipeline(numbers):
    sol = Solution()
    ans = sol.minCostClimbingStairs(*numbers)
    return ans


numbers = [[10,15,20]]
print( full_pipeline(numbers) )


str_list = [
    [[10,15,20]],
    [[1,100,1,1,1,100,1,1,100,1]],
    [[1,2,1,2,1,1,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )