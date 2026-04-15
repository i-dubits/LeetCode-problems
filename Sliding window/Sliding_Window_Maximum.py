
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq_dict = defaultdict(int)
        for ind in range(k):
            freq_dict[nums[ind]] += 1

        curr_arr = [-nums[ind] for ind in range(k)]

        heapq.heapify(curr_arr)
        ans.append(-curr_arr[0])

        for ind in range(k, len(nums)):
            old_el = nums[ind - k]
            freq_dict[old_el] -= 1

            new_el = nums[ind]
            freq_dict[new_el] += 1

            heapq.heappush(curr_arr, -new_el)
            loc_max = -curr_arr[0]
            while freq_dict[loc_max] <= 0:
                heapq.heappop(curr_arr)
                loc_max = -curr_arr[0]
            ans.append(loc_max)

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxSlidingWindow(*nums)
    return ans


numbers = [[1,3,-1,-3,5,3,6,7], 3]
print( full_pipeline(numbers) )


str_list = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1], 1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )