
from typing import List
from collections import defaultdict
import heapq


class Solution:


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []

        if k == 1:
            return nums

        if_odd = k % 2

        delayed = defaultdict(int)

        arr_k = sorted(nums[:k])

        left_max_arr = [-arr_k[ind] for ind in range(k//2)]
        right_min_arr = arr_k[k//2:]

        heapq.heapify(left_max_arr)
        heapq.heapify(right_min_arr)

        self.size_left, self.actual_size_left = len(left_max_arr), len(left_max_arr)
        self.size_right, self.actual_size_right = len(right_min_arr), len(right_min_arr)

        if if_odd:
            ans.append(right_min_arr[0])
        else:
            ans_curr = (right_min_arr[0] + (-left_max_arr[0])) / 2
            ans.append(ans_curr)

        for ind in range(k, len(nums)):

            # remove element
            el_to_remove = nums[ind - k]

            if el_to_remove >= right_min_arr[0]:
                delayed[el_to_remove] += 1
                self.actual_size_right -= 1
                self.prune_right_heap(right_min_arr, delayed)
            else:
                delayed[el_to_remove] += 1
                self.actual_size_left -= 1
                self.prune_left_heap(left_max_arr, delayed)

            # add element
            el_curr = nums[ind]
            if right_min_arr and el_curr >= right_min_arr[0]:
                heapq.heappush(right_min_arr, el_curr)
                self.actual_size_right += 1
                self.prune_right_heap(right_min_arr, delayed)
                self.balance(left_max_arr, right_min_arr, delayed)

            else:
                heapq.heappush(left_max_arr, -el_curr)
                self.actual_size_left += 1
                self.prune_left_heap(left_max_arr, delayed)
                self.balance(left_max_arr, right_min_arr, delayed)

            # compute median
            if if_odd:
                ans_curr = right_min_arr[0]
                ans.append(ans_curr)
            else:
                ans_right = right_min_arr[0]
                ans_left = -left_max_arr[0]
                ans_curr = (ans_left + ans_right) / 2
                ans.append(ans_curr)
        return ans


    def prune_right_heap(self, arr: list, delayed: dict):
        while arr and delayed[arr[0]] != 0:
            delayed[arr[0]] -= 1
            heapq.heappop(arr)

    def prune_left_heap(self, arr: list, delayed: dict):
        while arr and delayed[-arr[0]] != 0:
            delayed[-arr[0]] -= 1
            heapq.heappop(arr)

    def balance(self, left_max_arr, right_min_arr, delayed):
        if self.actual_size_right > self.size_right:
            self.prune_right_heap(right_min_arr, delayed)
            heapq.heappush(left_max_arr, -right_min_arr[0])
            self.actual_size_left += 1
            self.prune_left_heap(left_max_arr, delayed)

            heapq.heappop(right_min_arr)
            self.actual_size_right -= 1
            self.prune_right_heap(right_min_arr, delayed)

        if self.actual_size_left > self.size_left:
            self.prune_left_heap(left_max_arr, delayed)
            heapq.heappush(right_min_arr, -left_max_arr[0])
            self.actual_size_right += 1
            self.prune_right_heap(right_min_arr, delayed)

            heapq.heappop(left_max_arr)
            self.actual_size_left -= 1
            self.prune_left_heap(left_max_arr, delayed)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.medianSlidingWindow(*nums)
    return ans


# numbers = [[1,3,-1,-3,5,3,6,7], 3]
# numbers = [[4,1,7,1,8,7,8,7,7,4], 4]
numbers = [[1,2], 1]
print( full_pipeline(numbers) )


str_list = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1,2,3,4,2,3,1,4,2], 3],
    [[4,1,7,1,8,7,8,7,7,4], 4],
    [[2147483647,1,2,3,4,5,6,7,2147483647], 2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )