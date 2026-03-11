
from typing import List
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref_sum = []
        pref_sum_dict = defaultdict(int)

        for i, el in enumerate(nums):
            if el % k == 0 or el == 0:
                if i > 0 and (nums[i - 1] % k == 0 or nums[i - 1] == 0):
                    return True
                elif i < len(nums) - 1 and (nums[i + 1] % k == 0 or nums[i + 1] == 0):
                    return True
                else:
                    continue
            else:
                if len(pref_sum) != 0:
                    prev = pref_sum[-1]
                    pref_sum.append( (prev % k + el % k) % k )
                else:
                    pref_sum.append(el % k)

        for i, el in enumerate(pref_sum):
            pref_sum_dict[el] += 1
            if pref_sum_dict[el] > 1:
                return True
            if el == 0:
                return True

        return False


def full_pipeline(nums):

    sol = Solution()
    ans = sol.checkSubarraySum(*nums)
    return ans

# numbers = ["cbaebabacd", "abc"]
# numbers = [[23,2,4,6,7], 6]
# numbers = [[1,0,1,0,1], 4]
# numbers = [[5,0,0,0], 5]
numbers = [[50000000,50000000], 100000000]
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