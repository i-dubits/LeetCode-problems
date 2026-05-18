
from typing import List
from collections import defaultdict


class Solution:
    def isPalindrome(self, source: str) -> bool:

        source = source.lower()
        valid_digits = list( range(ord('0'), ord('9') + 1) )
        valid_letters = list( range(ord('a'), ord('z') + 1) )
        valid_symbols = valid_digits + valid_letters

        ans = True
        l = 0
        r = len(source) - 1
        while l < r:
            if ord(source[l]) not in valid_symbols:
                l += 1
                continue
            if ord(source[r]) not in valid_symbols:
                r -= 1
                continue

            if source[l] == source[r]:
                l += 1
                r -= 1
            else:
                ans = False
                return ans

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.isPalindrome(*nums)
    return ans

# numbers = ["A man, a plan, a canal: Panama"]
numbers = ["abc"]

print( full_pipeline(numbers) )


str_list = [
    ["A man, a plan, a canal: Panama"],
    ["race a car"],
    [" "],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )