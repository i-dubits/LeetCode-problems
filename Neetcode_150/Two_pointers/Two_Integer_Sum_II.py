
from typing import List


class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] + arr[r] < target:
                l += 1
            elif arr[l] + arr[r] > target:
                r -= 1
            elif arr[l] + arr[r] == target:
                break

        return [l+1, r+1]

def full_pipeline(numbers, k):
    sol = Solution()
    ans = sol.twoSum(numbers, k)
    # print(ans)
    return ans


numbers, k = [1,2,3,4], 3
print( full_pipeline(numbers, k) )


str_list = [
    [[1,2,3,4], 3],
#    [[], ],
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )