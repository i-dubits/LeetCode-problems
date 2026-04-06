
from typing import List
from collections import defaultdict
import heapq


class Solution:


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []

        if k == 1:
            return nums

        if_odd = k % 2
        arr_k = [ (nums[ind], ind) for ind in range(k)]
        arr_k = sorted(arr_k)

        left_max_arr = [ (-arr_k[ind][0], arr_k[ind][1]) for ind in range(k//2)]
        right_min_arr = arr_k[k//2:]

        heapq.heapify(left_max_arr)
        heapq.heapify(right_min_arr)

        self.size_left, self.actual_size_left = len(left_max_arr), len(left_max_arr)
        self.size_right, self.actual_size_right = len(right_min_arr), len(right_min_arr)

        if if_odd:
            ans.append(right_min_arr[0][0])
        else:
            ans_curr = (right_min_arr[0][0] + (-left_max_arr[0][0])) / 2
            ans.append(ans_curr)

        for ind in range(k, len(nums)):
            curr_el = (nums[ind], ind)
            first_window_ind = ind - k + 1

            el_to_compare = right_min_arr[0]
            self.prune_heap(left_max_arr, first_window_ind)
            self.prune_heap(right_min_arr, first_window_ind)

            el_to_remove = (nums[ind - k], ind - k)

            if el_to_remove >= el_to_compare:
                self.actual_size_right -= 1
            else:
                self.actual_size_left -= 1


            if curr_el >= el_to_compare:
                heapq.heappush(right_min_arr, curr_el)
                self.actual_size_right += 1

                if self.actual_size_right == self.size_right:
                    pass
                else:
                    if right_min_arr:
                        curr_tuple = heapq.heappop(right_min_arr)
                        self.actual_size_right -= 1
                        heapq.heappush(left_max_arr, (-curr_tuple[0], curr_tuple[1]))
                        self.actual_size_left += 1

            else:
                heapq.heappush(left_max_arr, (-curr_el[0], curr_el[1]))
                self.actual_size_left += 1
                if self.actual_size_left == self.size_left:
                    pass
                else:
                    if left_max_arr:
                        curr_tuple = heapq.heappop(left_max_arr)
                        self.actual_size_left -= 1
                        heapq.heappush(right_min_arr, (-curr_tuple[0], curr_tuple[1]))
                        self.actual_size_right += 1

            self.prune_heap(left_max_arr, first_window_ind)
            self.prune_heap(right_min_arr, first_window_ind)

            if if_odd:
                ans.append(right_min_arr[0][0])
            else:
                ans_curr = (right_min_arr[0][0] + (-left_max_arr[0][0])) / 2
                ans.append(ans_curr)

        return ans


    def prune_heap(self, arr: list, first_window_ind: int):
        while arr and arr[0][1] < first_window_ind:
            heapq.heappop(arr)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.medianSlidingWindow(*nums)
    return ans


# numbers = [[1,3,-1,-3,5,3,6,7], 3]
# numbers = [[2,2,2,1,2,2,2,2], 3]
numbers = [[1,3,-1,-3,5,3,6,7], 3]
# numbers = [[4,1,7,1,8,7,8,7,7,4], 4]
# numbers = [[1,2], 1]
print( full_pipeline(numbers) )


str_list = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1,2,3,4,2,3,1,4,2], 3],
    [[4,1,7,1,8,7,8,7,7,4], 4],
    [[2147483647,1,2,3,4,5,6,7,2147483647], 2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )