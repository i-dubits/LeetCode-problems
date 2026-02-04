
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


def full_pipeline(numbers):
    sol = Solution()
    ans = sol.maxArea(numbers)
    # print(ans)
    return ans


numbers = [1,7,2,5,4,7,3,6]
print( full_pipeline(numbers, k) )


str_list = [
    [1,7,2,5,4,7,3,6],
    [2,2,2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )