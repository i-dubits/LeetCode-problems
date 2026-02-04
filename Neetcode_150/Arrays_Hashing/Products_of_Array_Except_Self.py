
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * (len(nums))
        suffix_prod = [1] * (len(nums))

        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]

        rev_nums = list(reversed(nums))
        for i in range(1, len(rev_nums)):
            suffix_prod[i] = suffix_prod[i - 1] * rev_nums[i - 1]

        ans = []
        for k in range(len(nums)):
            arr_l = len(nums)
            ans.append(prefix_prod[k] * suffix_prod[arr_l - k - 1])

        return ans

def full_pipeline(nums):
    sol = Solution()
    ans = sol.productExceptSelf(nums)
    # print(ans)
    return ans

print( full_pipeline([1,2,4,6]) )


str_list = [
    [1,2,4,6],
    [-1,0,1,2,3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )