
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        tuple_list = [(interval.start, interval.end) for interval in intervals]
        tuple_sorted = sorted(tuple_list)

        curr_index = None
        for i, curr_tuple in enumerate(tuple_sorted):
            if curr_index is None:
                curr_index = i
                curr_end = curr_tuple[1]
            else:
                if curr_tuple[0] < curr_end:
                    return False
                else:
                    curr_index = i
                    curr_end = curr_tuple[1]


        return True



def full_pipeline(numbers):
    sol = Solution()

    list_int = [Interval(*t) for t in numbers]
    ans = sol.canAttendMeetings(list_int)
    return ans


# numbers = [(0,30),(5,10),(15,20)]
numbers = [(0,8),(8,10)]

print( full_pipeline(numbers) )


str_list = [
    [(0,30),(5,10),(15,20)],
    [(5,8),(9,15)],
    [(0,8),(8,10)]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )
