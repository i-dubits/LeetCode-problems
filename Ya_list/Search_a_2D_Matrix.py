
from typing import List
from collections import defaultdict


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.row_length = len(matrix[0])

        l = -1
        r = self.row_length * len(matrix)

        while l < r - 1:
            m = l + (r - l) // 2

            row_m, col_m = self.ind_to_multind(m)
            if matrix[row_m][col_m] < target:
                l = m
            else:
                r = m

        if r == self.row_length * len(matrix):
            return False

        row_r, col_r = self.ind_to_multind(r)
        if matrix[row_r][col_r] != target:
            return False
        else:
            return True


    def ind_to_multind(self, ind):
        row = ind // self.row_length
        col = ind % self.row_length
        return row, col


def full_pipeline(nums):

    sol = Solution()
    ans = sol.searchMatrix(*nums)
    return ans

numbers = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3]
print( full_pipeline(numbers) )


str_list = [
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )