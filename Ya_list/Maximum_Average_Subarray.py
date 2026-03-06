
from typing import List
import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        aver_curr = sum(nums[:k])/k
        ans = aver_curr

        for i in range(k, len(nums)):
            aver_curr -= nums[i - k]/k
            aver_curr += nums[i]/k
            ans = max(ans, aver_curr)

        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.findMaxAverage(*nums)
    return ans

numbers = [[1,12,-5,-6,50,3], 4]
print( full_pipeline(numbers) )


str_list = [
    [[1,12,-5,-6,50,3], 4],
    [[5], 1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )