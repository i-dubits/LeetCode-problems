
from typing import List
from collections import defaultdict
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = math.inf
        ans = 0

        for price in prices:
            if price <= curr_min:
                curr_min = price
            else:
                ans = max(ans, price - curr_min)

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxProfit(*nums)
    return ans


numbers = [[7,1,5,3,6,4]]

print( full_pipeline(numbers) )


str_list = [
    [[7,1,5,3,6,4]],
    [[7,6,4,3,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )