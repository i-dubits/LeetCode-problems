
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0

        begin = None
        in_segm = False
        for i in range(len(nums)):
            if nums[i] == 1:
                if in_segm:
                    continue
                else:
                    in_segm = True
                    begin = i
            else:
                if in_segm:
                    curr = i - begin
                    ans = max(ans, curr)

                    in_segm = False
                    begin = None
                else:
                    continue

        if in_segm:
            curr = len(nums) - begin
            ans = max(ans, curr)

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.findMaxConsecutiveOnes(nums)
    return ans

numbers = [1,1,0,1,1,1]

print( full_pipeline(numbers) )


str_list = [
    [1,1,0,1,1,1],
    [1,0,1,1,0,1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )