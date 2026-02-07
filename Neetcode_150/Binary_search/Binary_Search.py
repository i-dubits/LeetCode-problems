from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)

        while l < r - 1:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m
            else:
                r = m

        if r > len(nums) - 1 or nums[r] != target:
            return -1
        else:
            return r

def full_pipeline(numbers, target):
    sol = Solution()
    ans = sol.search(numbers, target)
    # print(ans)
    return ans


numbers, target = [-1,0,2,4,6,8], 4
# numbers = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
# numbers = [1,2,1]

print( full_pipeline(numbers, target) )


str_list = [
    [[-1,0,2,4,6,8], 4],
    [[-1,0,2,4,6,8], 3],
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )