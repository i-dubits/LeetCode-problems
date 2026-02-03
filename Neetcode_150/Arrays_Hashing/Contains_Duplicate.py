
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            else:
                my_set.add(num)

        return False


def full_pipeline(nums: List[int]) -> bool:
    sol = Solution()
    ans = sol.hasDuplicate(nums)
    # print(ans)
    return ans

nums_list = [[1, 2, 3, 3],
             [1, 2, 3, 4]]

for nums in nums_list:
    print(full_pipeline(nums))


