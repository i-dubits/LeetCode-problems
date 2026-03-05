
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for num in nums:
            if num == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt += 1

        res = max(res, cnt)
        return res

def full_pipeline(nums):

    sol = Solution()
    ans = sol.findMaxConsecutiveOnes(nums)
    return ans

numbers = [1,1,0,1,1,1]

print( full_pipeline(numbers) )


str_list = [
    [1,1,0,1,1,1],
    [1,0,1,1,0,1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )