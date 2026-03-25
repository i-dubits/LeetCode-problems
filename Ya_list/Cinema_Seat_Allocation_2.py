
from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0

        row_to_slots = [[] for i in range(n+1)]

        for slot in reservedSeats:
            row_to_slots[slot[0]].append(slot[1])

        for i in range(1, n+1):
            if len(row_to_slots[i]) == 0:
                ans += 2
            else:
                dec_arr = [True, True, True]
                for el in row_to_slots[i]:
                    if el in [2,3,4,5]:
                        dec_arr[0] = False
                    if el in [4,5,6,7]:
                        dec_arr[1] = False
                    if el in [6,7,8,9]:
                        dec_arr[2] = False

                if dec_arr[0] is True:
                    dec_arr[1] = False
                if dec_arr[1] is True:
                    dec_arr[2] = False

                ans += sum(dec_arr)

        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxNumberOfFamilies(*nums)
    return ans

# numbers = [3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]]
numbers = [2, [[1,6],[1,8],[1,3],[2,3],[1,10],[1,2],[1,5],[2,2],[2,4],[2,10],[1,7],[2,5]]]
print( full_pipeline(numbers) )


str_list = [
    [3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]],
    [2, [[2,1],[1,8],[2,6]]],
    [4, [[4,3],[1,4],[4,6],[1,7]]],
    [2, [[1,6],[1,8],[1,3],[2,3],[1,10],[1,2],[1,5],[2,2],[2,4],[2,10],[1,7],[2,5]]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )