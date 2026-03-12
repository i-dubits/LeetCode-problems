
from typing import List
from collections import defaultdict


class Solution:
    def maxVowels(self, source: str, k: int) -> int:
        vowels = set(('a', 'e', 'i', 'o', 'u'))

        ans = 0
        curr_count = sum([1 for ch_curr in source[:k] if ch_curr in vowels])
        ans = max(ans, curr_count)

        for r in range(k, len(source)):
            if source[r] in vowels:
                curr_count += 1
            if source[r - k] in vowels:
                curr_count -= 1
            ans = max(ans, curr_count)

            if ans == k:
                return ans

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.maxVowels(*nums)
    return ans

# numbers = ["abciiidef", 3]
numbers = ["leetcode", 3]
print( full_pipeline(numbers) )


str_list = [
    ["abciiidef", 3],
    ["aeiou", 2],
    ["leetcode", 3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )