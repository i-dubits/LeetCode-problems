from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        init_set = set(nums)

        start_points = []
        max_len = 0

        for num in init_set:
            if num - 1 not in init_set:
                start_points.append(num)

        for start_point in start_points:
            curr_len = 1
            curr_point = start_point
            while True:
                if curr_point + 1 in init_set:
                    curr_point += 1
                    curr_len += 1
                else:
                    break

            max_len = max(max_len, curr_len)

        return max_len


def full_pipeline(nums):
    sol = Solution()
    ans = sol.longestConsecutive(nums)
    # print(ans)
    return ans

print( full_pipeline([9,1,4,7,3,-1,0,5,8,-1,6]) )


str_list = [
    [2,20,4,10,3,4,5],
    [0,3,2,5,4,6,1,1],
    [9,1,4,7,3,-1,0,5,8,-1,6],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )