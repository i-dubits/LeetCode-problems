
from typing import List
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref_sum = nums[0] % k
        pref_hash = defaultdict(int)

        if len(nums) == 1:
            return False

        pref_hash[pref_sum] = 0
        for i in range(1, len(nums)):
            pref_sum = (pref_sum % k + nums[i] % k) % k
            if pref_sum == 0:
                return True
            if pref_sum in pref_hash:
                ind_prev = pref_hash[pref_sum]
                if i - ind_prev >= 2:
                    return True
            else:
                pref_hash[pref_sum] = i

        if pref_sum == 0:
            return True

        return False


def full_pipeline(nums):

    sol = Solution()
    ans = sol.checkSubarraySum(*nums)
    return ans

# numbers = [[23,2,4,6,7], 6]
# numbers = [[1,0,1,0,1], 4]
# numbers = [[5,0,0,0], 5]
numbers = [[23,2,4,6,6], 7]
# numbers = [[50000000,50000000], 100000000]
print( full_pipeline(numbers) )


str_list = [
    [[23,2,4,6,7], 6],
    [[23,2,6,4,7], 6],
    [[23,2,6,4,7], 13],
    [[1,0,1,0,1], 4],
    [[5,0,0,0], 5],
    [[50000000,50000000], 100000000],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )