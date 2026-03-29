
from typing import List
from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_ns = 0
        dp_s = -prices[0]

        if len(prices) == 0:
            return 0

        for ind in range(1, len(prices)):
            dp_ns = max(dp_ns, dp_s + prices[ind])
            dp_s = max(dp_s, dp_ns - prices[ind])

        return max(dp_ns, 0)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxProfit(*nums)
    return ans


numbers = [[7,1,5,3,6,4]]

print( full_pipeline(numbers) )


str_list = [
    [[7,1,5,3,6,4]],
    [[1,2,3,4,5]],
    [[7,6,4,3,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )