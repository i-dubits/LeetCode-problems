from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        curr_min = prices[0]
        max_profit = 0

        for r in range(1, len(prices)):
            if curr_min > prices[r]:
                curr_min = prices[r]
            else:
                curr_profit = prices[r] - curr_min
                max_profit = max(max_profit, curr_profit)

        return max_profit




def full_pipeline(numbers):
    sol = Solution()
    ans = sol.maxProfit(numbers)
    # print(ans)
    return ans


numbers = [10,1,5,6,7,1]
# numbers = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
# numbers = [1,2,1]

print( full_pipeline(numbers) )


str_list = [
    [10,1,5,6,7,1],
    [10,8,7,5,2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )