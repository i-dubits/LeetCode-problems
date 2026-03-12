
from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans = 0

        nums = [el%2 for el in nums]
        pref_sum = [0]*(len(nums) + 1)

        for i in range(1, len(nums) + 1):
            pref_sum[i] = pref_sum[i - 1] + nums[i - 1]

        l = 0
        freq_count = defaultdict(int)
        freq_count[0] = 1
        for r in range(1, len(nums) + 1):

            freq_count[pref_sum[r]] += 1
            while l <= r and pref_sum[r] - pref_sum[l] > k:
                l += 1
            if pref_sum[r] - pref_sum[l] == k:
                ans += freq_count[pref_sum[l]]

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