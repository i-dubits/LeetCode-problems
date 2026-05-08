
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ind_1 = 0
        ind_2 = 0

        ans = []

        while ind_1 < len(firstList) and ind_2 < len(secondList):

            b1, e1 = firstList[ind_1][0], firstList[ind_1][1]
            b2, e2 = secondList[ind_2][0], secondList[ind_2][1]
            res_int = self.section_intersec(firstList[ind_1], secondList[ind_2])
            if len(res_int) == 0:
                if e1 < b2:
                    ind_1 += 1
                else:
                    ind_2 += 1

            else:
                ans.append(res_int)
                bi, ei = res_int[0], res_int[1]
                if ei == e1:
                    ind_1 += 1
                elif ei == e2:
                    ind_2 += 1
                else:
                    print('something is wrong')

        return ans


    def section_intersec(self, sect_1: list, sect_2: list ) -> list:
        b1, e1 = sect_1[0], sect_1[1]
        b2, e2 = sect_2[0], sect_2[1]
        if e1 < b2 or e2 < b1:
            return []

        b_i = max(b1, b2)
        e_i = min(e1, e2)
        return [b_i, e_i]

def full_pipeline(nums):

    sol = Solution()
    ans = sol.intervalIntersection(*nums)
    return ans

numbers = [[[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]]
print( full_pipeline(numbers) )


str_list = [
    [[[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]],
    [[[1,3],[5,9]], []],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )