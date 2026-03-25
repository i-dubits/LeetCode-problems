
from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0

        curr_row = 1
        curr_row_slots = []

        reservedSeats = sorted(reservedSeats)

        curr_slot_ind = 0
        while curr_slot_ind < len(reservedSeats):
            if reservedSeats[curr_slot_ind][0] == curr_row:
                curr_row_slots.append(reservedSeats[curr_slot_ind][1])
            else:
                ans += self.process_row(curr_row_slots)

                ans += (reservedSeats[curr_slot_ind][0] - curr_row - 1) * 2

                curr_row_slots = []
                curr_row_slots.append(reservedSeats[curr_slot_ind][1])
                curr_row = reservedSeats[curr_slot_ind][0]
            curr_slot_ind += 1

        ans += self.process_row(curr_row_slots)

        ans += (n - curr_row)*2

        return ans

    def process_row(self, curr_row_slots):
        curr_row_slots = sorted(curr_row_slots)
        avail_dict = {2: True, 4:True, 6:True}
        for slot in curr_row_slots:
            if slot in [2,3,4,5]:
                avail_dict[2] = False
            if slot in [4,5,6,7]:
                avail_dict[4] = False
            if slot in [6,7,8,9]:
                avail_dict[6] = False

        if avail_dict[2]:
            avail_dict[4] = False
        if avail_dict[4]:
            avail_dict[6] = False

        ans = 0
        for value in avail_dict.values():
            ans += int(value)
        return ans


def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxNumberOfFamilies(*nums)
    return ans

numbers = [3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]]
print( full_pipeline(numbers) )


str_list = [
    [3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]],
    [2, [[2,1],[1,8],[2,6]]],
    [4, [[4,3],[1,4],[4,6],[1,7]]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )