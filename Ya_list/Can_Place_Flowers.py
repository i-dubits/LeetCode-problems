
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
            if n <= 0:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            else:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        if n <= 0:
            return True
        else:
            return False



def full_pipeline(nums):

    sol = Solution()
    ans = sol.canPlaceFlowers(*nums)
    return ans

numbers = [[1,0,0,0,0,1], 2]

print( full_pipeline(numbers) )


str_list = [
    [[1,0,0,0,1], 1],
    [[1,0,0,0,1], 2],
    [[1,0,0,0,0,1], 2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )