
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        el_to_pos = {}

        for pos, el in enumerate(nums):
            el_to_pos[el] = pos

        ans = []
        for current_pos, curr_el in enumerate(nums):
            check_el = target - curr_el
            if check_el in el_to_pos and el_to_pos[check_el] != current_pos:
                ans = sorted([current_pos, el_to_pos[check_el]])
                return ans
            else:
                continue



def full_pipeline(nums, target):
    sol = Solution()
    ans = sol.twoSum(nums, target)
    # print(ans)
    return ans

str_list = [
    [[3,4,5,6], 7],
    [[4,5,6], 10],
    [[5,5], 10]
]

for str_pair in str_list:
    nums, target = str_pair
    print(full_pipeline(nums, target))