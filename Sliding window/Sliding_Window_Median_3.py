
from typing import List
from collections import defaultdict
import heapq


class MinHeap:
    def __init__(self):
        self.arr = []

    def push_el(self, el: int):
        if len(self.arr) == 0:
            self.arr.append(el)
            return

        self.arr.append(el)
        self.sift_up( len(self.arr) - 1 )

    def sift_up(self, ind: int):

        curr_ind = ind
        if curr_ind == 0:
            return
        pred_ind = (curr_ind - 1) // 2

        while self.arr[curr_ind] < self.arr[pred_ind]:
            self.arr[curr_ind], self.arr[pred_ind] = self.arr[pred_ind], self.arr[curr_ind]

            if pred_ind == 0:
                return
            curr_ind = pred_ind
            pred_ind = (curr_ind - 1) // 2

    def sift_down(self, ind):
        left_child_ind = 2*ind + 1
        right_child_ind = 2*ind + 2

        while left_child_ind < len(self.arr):
            if right_child_ind < len(self.arr):
                if (self.arr[ind] > self.arr[left_child_ind]
                    or self.arr[ind] > self.arr[right_child_ind]):
                    if self.arr[left_child_ind] > self.arr[right_child_ind]:
                        self.arr[ind], self.arr[right_child_ind] = self.arr[right_child_ind], self.arr[ind]
                        ind = right_child_ind
                    else:
                        self.arr[ind], self.arr[left_child_ind] = self.arr[left_child_ind], self.arr[ind]
                        ind = left_child_ind
                else:
                    return
            else:
                if self.arr[ind] > self.arr[left_child_ind]:
                    self.arr[ind], self.arr[left_child_ind] = self.arr[left_child_ind], self.arr[ind]
                    ind = left_child_ind
                else:
                    return

            left_child_ind = 2 * ind + 1
            right_child_ind = 2 * ind + 2

    def remove_by_ind(self, ind: int):
        self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
        self.arr.pop()

        if ind == len(self.arr):
            return
        if ind == 0:
            self.sift_down(ind)
            return
        if self.arr[ind] < self.arr[(ind - 1)//2]:
            self.sift_up(ind)
            return
        else:
            self.sift_down(ind)
            return


class MinHeapInd:
    """
    Heap stores the indices of the initial array for the sliding median problem
    """
    def __init__(self, nums: list):
        self.heap = []
        self.nums = nums

        self.pos = {} # nums index to heap (heap) index

    def __len__(self):
        return len(self.heap)

    def get_value_from_heap_ind(self, heap_ind: int) -> int:
        value = self.nums[self.heap[heap_ind]]
        return value

    def if_first_less_second(self, first_ind_heap: int, second_ind_heap: int) -> bool:

        first_val = self.get_value_from_heap_ind(first_ind_heap)
        second_val = self.get_value_from_heap_ind(second_ind_heap)

        if first_val < second_val:
            return True
        else:
            return False

    def swap_els(self, first_ind_heap: int, second_ind_heap: int):
        self.pos[self.heap[first_ind_heap]], self.pos[self.heap[second_ind_heap]] = \
            self.pos[self.heap[second_ind_heap]], self.pos[self.heap[first_ind_heap]]

        self.heap[first_ind_heap], self.heap[second_ind_heap] = \
            self.heap[second_ind_heap], self.heap[first_ind_heap]


    def push_el(self, el: int):
        if len(self.heap) == 0:
            self.heap.append(el)
            self.pos[el] = len(self.heap) - 1
            return

        self.heap.append(el)
        self.pos[el] = len(self.heap) - 1
        self.sift_up( len(self.heap) - 1 )

    def sift_up(self, ind: int):

        curr_ind = ind
        if curr_ind == 0:
            return
        pred_ind = (curr_ind - 1) // 2

        while self.if_first_less_second(curr_ind, pred_ind):
            self.swap_els(curr_ind, pred_ind)
            if pred_ind == 0:
                return
            curr_ind = pred_ind
            pred_ind = (curr_ind - 1) // 2


    def sift_down(self, ind):
        left_child_ind = 2*ind + 1
        right_child_ind = 2*ind + 2

        while left_child_ind < len(self.heap):
            if right_child_ind < len(self.heap):
                if (self.if_first_less_second(left_child_ind, ind)
                    or self.if_first_less_second(right_child_ind, ind)):

                    if self.if_first_less_second(right_child_ind, left_child_ind):
                        self.swap_els(ind, right_child_ind)
                        ind = right_child_ind

                    else:
                        self.swap_els(ind, left_child_ind)
                        ind = left_child_ind
                else:
                    return
            else:
                if self.if_first_less_second(left_child_ind, ind):
                    self.swap_els(ind, left_child_ind)
                    ind = left_child_ind
                else:
                    return

            left_child_ind = 2 * ind + 1
            right_child_ind = 2 * ind + 2

    def remove_by_ind(self, ind: int):
        self.swap_els(ind, -1)
        del self.pos[self.heap[-1]]
        self.heap.pop()

        if ind == len(self.heap):
            return
        if ind == 0:
            self.sift_down(ind)
            return

        if self.if_first_less_second(ind, (ind - 1)//2):
            self.sift_up(ind)
            return
        else:
            self.sift_down(ind)
            return


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []

        if k == 1:
            return nums

        if_odd = k % 2
        arr_k = [(nums[ind], ind) for ind in range(k)]
        arr_k = sorted(arr_k)

        left_max_heap = MinHeapInd([-el for el in nums])
        right_min_heap = MinHeapInd(nums)

        for el in arr_k[k//2:]:
            val, ind_nums = el
            right_min_heap.push_el(ind_nums)

        for el in arr_k[:k//2]:
            val, ind_nums = el
            left_max_heap.push_el(ind_nums)

        self.size_left, self.actual_size_left = len(left_max_heap), len(left_max_heap)
        self.size_right, self.actual_size_right = len(right_min_heap), len(right_min_heap)

        if if_odd:
            val = nums[right_min_heap.heap[0]]
            ans.append(val)
        else:
            val_1, val_2 = nums[right_min_heap.heap[0]], nums[left_max_heap.heap[0]]
            ans_curr = (val_1 + val_2) / 2
            ans.append(ans_curr)

        for ind_nums_to_add in range(k, len(nums)):

            ind_nums_to_remove = ind_nums_to_add - k
            el_to_add = nums[ind_nums_to_add]

            if ind_nums_to_remove in left_max_heap.pos:
                heap_ind_to_remove = left_max_heap.pos[ind_nums_to_remove]
                left_max_heap.remove_by_ind(heap_ind_to_remove)

                el_to_compare = nums[right_min_heap.heap[0]] if len(right_min_heap.heap) != 0\
                    else nums[left_max_heap.heap[0]]

                if el_to_add > el_to_compare:
                    right_min_heap.push_el(ind_nums_to_add)
                    # balance heaps
                    ind_to_balance = right_min_heap.heap[0]
                    right_min_heap.remove_by_ind(0)
                    left_max_heap.push_el(ind_to_balance)

                else:
                    left_max_heap.push_el(ind_nums_to_add)

            elif ind_nums_to_remove in right_min_heap.pos:
                heap_ind_to_remove = right_min_heap.pos[ind_nums_to_remove]
                right_min_heap.remove_by_ind(heap_ind_to_remove)

                el_to_compare = nums[right_min_heap.heap[0]] if len(right_min_heap.heap) != 0\
                    else nums[left_max_heap.heap[0]]

                if el_to_add > el_to_compare:
                    right_min_heap.push_el(ind_nums_to_add)

                else:
                    left_max_heap.push_el(ind_nums_to_add)
                    # balance heaps
                    ind_to_balance = left_max_heap.heap[0]
                    left_max_heap.remove_by_ind(0)
                    right_min_heap.push_el(ind_to_balance)

            else:
                print(f'Element to remove is missing!')

            if if_odd:
                val = nums[right_min_heap.heap[0]]
                ans.append(val)
            else:
                val_1, val_2 = nums[right_min_heap.heap[0]], nums[left_max_heap.heap[0]]
                ans_curr = (val_1 + val_2) / 2
                ans.append(ans_curr)

        return ans


def full_pipeline(nums):

    sol = Solution()
    ans = sol.medianSlidingWindow(*nums)
    return ans


# numbers = [[1,3,-1,-3,5,3,6,7], 3]
# numbers = [[2,2,2,1,2,2,2,2], 3]
# numbers = [[1,3,-1,-3,5,3,6,7], 3]
# numbers = [[4,1,7,1,8,7,8,7,7,4], 4]
# numbers = [[1,2], 1]
numbers = [[1,4,2,3], 4]
print( full_pipeline(numbers) )


str_list = [
    [[1,3,-1,-3,5,3,6,7], 3],
    [[1,2,3,4,2,3,1,4,2], 3],
    [[4,1,7,1,8,7,8,7,7,4], 4],
    [[2147483647,1,2,3,4,5,6,7,2147483647], 2],
    [[1,4,2,3], 4]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )