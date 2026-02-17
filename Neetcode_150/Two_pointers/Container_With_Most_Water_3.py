
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ans = 0

        l = 0
        r = len(heights) - 1

        ans = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            curr_vol = min(heights[l], heights[r]) * (r - l)
            ans = max(curr_vol, ans)

        if l != r:
            middle_vol = min(heights[l], heights[r]) * (r - l)
            ans = max(middle_vol, ans)

        return ans


def full_pipeline(numbers):
    sol = Solution()
    ans = sol.maxArea(numbers)
    # print(ans)
    return ans


numbers = [1,7,2,5,4,7,3,6]
# numbers = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
# numbers = [1,2,1]

print( full_pipeline(numbers) )


str_list = [
    [1,7,2,5,4,7,3,6],
    [2,2,2],
    [1,2,1],
    [1,7,2,5,12,3,500,500,7,8,4,7,3,6],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )