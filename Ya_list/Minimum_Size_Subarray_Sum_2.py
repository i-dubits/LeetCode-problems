
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pref_sum = self.prefix_sum(nums)

        min_len = len(nums) + 1

        min_len_all = self.bin_search(pref_sum, target, l_init=-1, r_init=len(nums)+1)
        if min_len_all != -1:
            min_len = min(min_len, min_len_all)

        for start in range(1, len(nums)):
            curr_target = target + pref_sum[start]
            # ind_curr = self.bin_search(pref_sum[start+1:], curr_target)
            ind_curr = self.bin_search(pref_sum, curr_target, l_init=start, r_init=len(nums)+1)
            if ind_curr != -1:
                len_curr = ind_curr - start
                min_len = min(min_len, len_curr)

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len

    def prefix_sum(self, nums):
        pref_s = [0]*(len(nums) + 1)

        for i in range(1, len(nums) + 1):
            pref_s[i] += pref_s[i-1] + nums[i-1]

        return pref_s

    def bin_search(self, arr, target, l_init, r_init):
        l = l_init
        r = r_init

        while l < r - 1:
            m = l + (r - l) // 2
            if arr[m] < target:
                l = m
            else:
                r = m

        if r == r_init or arr[r] < target:
            return -1
        else:
            return r



def full_pipeline(nums):

    sol = Solution()
    ans = sol.minSubArrayLen(*nums)
    return ans

# numbers = [10, [2,1,5,1,5,3]]
# numbers = [4, [1,4,4]]
numbers = [10, [1,2,3,4]]
# numbers = [7, [2,3,1,2,4,3]]
# numbers = [5, [1,2,1]]

print( full_pipeline(numbers) )


str_list = [
    [10, [2,1,5,1,5,3]],
    [5, [1,2,1]],
    [7, [2,3,1,2,4,3]],
    [4, [1,4,4]],
    [11, [1,1,1,1,1,1,1,1]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )