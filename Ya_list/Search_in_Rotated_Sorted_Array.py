
from typing import List
from collections import defaultdict


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.n = len(nums)

        l = -1
        r = len(nums)
        leftmost = nums[0]

        while l < r - 1:
            m = l + (r - l) // 2

            if leftmost <= nums[m]:
                l = m
            else:
                r = m
            leftmost = nums[l]

        if l == -1:
            infl_point = r
        elif r == len(nums):
            infl_point = l
        else:
            infl_point = l


        target_left = self.bin_search(l=-1, r=infl_point + 1, target=target)
        target_right = self.bin_search(l=infl_point, r=len(nums), target=target)

        ans = target_left if target_left != -1 else target_right
        return ans

    def bin_search(self, l, r, target):

        l_init = l
        r_init = r

        while l < r - 1:
            m = l + (r - l) // 2

            if self.nums[m] < target:
                l = m
            else:
                r = m

        if r == r_init:
            return -1
        if self.nums[r] != target:
            return -1
        else:
            return r

def full_pipeline(nums):

    sol = Solution()
    ans = sol.search(*nums)
    return ans

numbers = [[3,1], 1]
print( full_pipeline(numbers) )


str_list = [
    [[4,5,6,7,0,1,2], 0],
    [[4,5,6,7,0,1,2], 3],
    [[1], 0],
    [[3,1], 1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )