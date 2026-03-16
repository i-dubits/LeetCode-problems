
from typing import List
from collections import defaultdict

from prompt_toolkit.contrib.telnet import TelnetServer


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pref_sum = [0] * (len(nums) + 1)
        pref_to_freq_dict = defaultdict(int)
        ans = 0

        pref_to_freq_dict[pref_sum[0]] = 1

        for ind, val in enumerate(nums):

            pref_sum[ind + 1] = pref_sum[ind] + nums[ind]

            local_target = pref_sum[ind + 1] - k
            if local_target in pref_to_freq_dict:
                ans += pref_to_freq_dict[local_target]
            pref_to_freq_dict[pref_sum[ind + 1]] += 1

        return ans


def full_pipeline(nums):

    sol = Solution()
    ans = sol.subarraySum(*nums)
    return ans

# numbers = [[2,-1,1,2], 2]
numbers = [[-1,-1,1], 0]

print( full_pipeline(numbers) )


str_list = [
    [[2,-1,1,2], 2],
    [[4,4,4,4,4,4], 4],
    [[1,1,1], 2],
    [[1,2,3], 3],
    [[-1,-1,1], 0]

]

for str_curr in str_list:
    print( full_pipeline(str_curr) )