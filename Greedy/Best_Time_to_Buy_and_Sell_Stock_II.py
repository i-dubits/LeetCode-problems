
from typing import List
from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        if len(prices) == 1:
            return total

        price_beg = prices[0]
        price_end = None
        for i in range(1, len(prices)):
            curr_pr = prices[i]
            if curr_pr >= prices[i - 1]:
                price_end = curr_pr
            else:
                if price_end is not None:
                    total += price_end - price_beg
                price_beg = curr_pr
                price_end = None

        if price_end is not None:
            total += price_end - price_beg

        return total

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