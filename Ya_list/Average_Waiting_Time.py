
from typing import List
from collections import defaultdict


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time_curr = 0
        wait_time = [None] * len(customers)

        for ind, cust in enumerate(customers):
            arrival_time = cust[0]
            cook_time_curr = cust[1]

            if finish_time_curr <= arrival_time:
                finish_time_curr = arrival_time + cook_time_curr
            else:
                finish_time_curr += cook_time_curr

            wait_time[ind] = finish_time_curr - arrival_time

        average = sum(wait_time) / len(customers)
        return average

def full_pipeline(nums):

    sol = Solution()
    ans = sol.averageWaitingTime(*nums)
    return ans

numbers = [[[1,2],[2,5],[4,3]]]
print( full_pipeline(numbers) )


str_list = [
    [[[1,2],[2,5],[4,3]]],
    [[[5,2],[5,4],[10,3],[20,1]]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )