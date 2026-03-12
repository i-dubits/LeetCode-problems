
from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        for ind_1 in range(len(nums)):
            freq_dict[nums[ind_1]] -= 1
            if freq_dict[nums[ind_1]] < 0:
                freq_dict[nums[ind_1]] += 1
                continue
            for ind_2 in range(ind_1, len(nums)):
                freq_dict[nums[ind_2]] -= 1
                if freq_dict[nums[ind_2]] < 0:
                    freq_dict[nums[ind_2]] += 1
                    continue
                for ind_3 in range(ind_2, len(nums)):
                    freq_dict[nums[ind_3]] -= 1
                    if freq_dict[nums[ind_3]] < 0:
                        freq_dict[nums[ind_3]] += 1
                        continue
                    fourth_el = target - (nums[ind_1] + nums[ind_2] + nums[ind_3])
                    if freq_dict[fourth_el] > 0:
                        curr_tuple = tuple(sorted([nums[ind_1], nums[ind_2], nums[ind_3], fourth_el]))
                        ans.add(curr_tuple)

                    freq_dict[nums[ind_3]] += 1
                freq_dict[nums[ind_2]] += 1
            freq_dict[nums[ind_1]] += 1

        return list(ans)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.fourSum(*nums)
    return ans

numbers = [[1,0,-1,0,-2,2], 0]
# numbers = [[2,2,2,2,2], 8]
print( full_pipeline(numbers) )


str_list = [
    [[1,0,-1,0,-2,2], 0],
    [[2,2,2,2,2], 8],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )