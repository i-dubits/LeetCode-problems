
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        max_h_ind = self.find_peak_right_most(height)
        if max_h_ind == -1:
            return 0

        prev_max_h = height[0]
        for i in range(1, max_h_ind):
            curr_h = height[i]
            if curr_h >= prev_max_h:
                prev_max_h = curr_h
            else:
                ans += prev_max_h - curr_h

        prev_max_h = height[-1]
        for i in range(len(height) - 1, max_h_ind, -1):
            curr_h = height[i]
            if curr_h >= prev_max_h:
                prev_max_h = curr_h
            else:
                ans += prev_max_h - curr_h

        return ans


    def find_peak_right_most(self, height: List[int]) -> int:
        curr_max_h = 0
        curr_max_h_ind = -1

        for ind_curr, h_curr in enumerate(height):
            if h_curr >= curr_max_h:
                curr_max_h_ind = ind_curr
                curr_max_h = h_curr

        return curr_max_h_ind

def full_pipeline(numbers):
    sol = Solution()
    ans = sol.trap(numbers)
    # print(ans)
    return ans


numbers = [0,2,0,3,1,0,1,3,2,1]
# numbers = [0,1,0,2,1,0,1,3,2,1,2,1]
# numbers = [4,2,0,3,2,5]
print( full_pipeline(numbers) )


str_list = [
    [0,2,0,3,1,0,1,3,2,1],
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )