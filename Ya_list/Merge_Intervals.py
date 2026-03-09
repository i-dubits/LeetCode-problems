
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interv_sorted = sorted(intervals)

        ans = []

        if len(interv_sorted) == 1:
            return intervals

        beg_prev = interv_sorted[0][0]
        end_prev = interv_sorted[0][1]

        for interval in interv_sorted[1:]:
            if end_prev >= interval[0]:
                end_prev = max(end_prev, interval[1])
            else:
                ans.append([beg_prev, end_prev])
                beg_prev = interval[0]
                end_prev = interval[1]

        ans.append([beg_prev, end_prev])
        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.merge(nums)
    return ans

numbers = [[1,3],[1,5],[6,7]]

print( full_pipeline(numbers) )


str_list = [
    [[1,3],[1,5],[6,7]],
    [[1,2],[2,3]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )