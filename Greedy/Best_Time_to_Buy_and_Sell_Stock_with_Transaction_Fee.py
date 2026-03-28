
from typing import List
from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_s = [0] * len(prices)
        dp_ns = [0] * len(prices)

        if len(prices) == 1:
            return 0

        dp_s[0] = -prices[0]
        dp_ns[0] = 0

        for i in range(1, len(prices)):
            dp_s[i] = max(dp_s[i - 1], dp_ns[i-1] - prices[i])
            dp_ns[i] = max(dp_ns[i-1],  dp_s[i-1] + prices[i] - fee)

        return max(dp_s[-1], dp_ns[-1])



def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxProfit(*nums)
    return ans


numbers = [[1,3,2,8,4,9], 2]
# numbers = [[1,3,7,5,10,3], 3]
# numbers = [[4,5,2,4,3,3,1,2,5,4], 1]
# numbers = [[2,2,1,1,5], 2]
# numbers = [[1, 4, 2, 3], 2]
# numbers = [[2,2,1,1,5,5,3,1,5,4], 2]
# numbers = [[4,5,2,4,3,3], 1]
# numbers = [[1,2,5,4], 1]

print( full_pipeline(numbers) )


str_list = [
    [[1,3,2,8,4,9], 2],
    [[1,3,7,5,10,3], 3],
    [[4,5,2,4,3,3,1,2,5,4], 1]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )