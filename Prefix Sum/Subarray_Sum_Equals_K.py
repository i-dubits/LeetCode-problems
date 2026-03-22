
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        pref_sum = [0] * (len(nums) + 1)
        freq_dict = defaultdict(int)
        freq_dict[pref_sum[0]] += 1

        for i in range(1, len(nums) + 1):
            pref_sum[i] = pref_sum[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            curr_target = pref_sum[i + 1] - k
            if curr_target in freq_dict:
                ans += freq_dict[curr_target]
            freq_dict[pref_sum[i + 1]] += 1

        return ans


def full_pipeline(numbers):
    sol = Solution()
    ans = sol.subarraySum(*numbers)
    return ans


numbers = [[1,1,1], 2]
print( full_pipeline(numbers) )


str_list = [
    [[1,1,1], 2],
    [[1,2,3], 3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )