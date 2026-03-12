
from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans = 0

        nums = [el%2 for el in nums]
        pref_sum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            pref_sum[i] = pref_sum[i-1] + nums[i-1]

        freqs = defaultdict(int)

        for curr_sum in pref_sum:
            des_sum = curr_sum - k
            if des_sum in freqs:
               ans += freqs[des_sum]
            freqs[curr_sum] += 1

        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.numberOfSubarrays(*nums)
    return ans

numbers = [[1,1,2,1,1], 3]
print( full_pipeline(numbers) )


str_list = [
    [[1,1,2,1,1], 3],
    [[2,4,6], 1],
    [[2,2,2,1,2,2,1,2,2,2], 2]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )