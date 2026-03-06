from typing import List


class Solution:
    def lengthOfLongestSubstring(self, my_str: str) -> int:
        my_set = set()

        ans = 0
        l = 0
        n = len(my_str)
        for r in range(n):
            while l < n and my_str[r] in my_set:
                my_set.remove(my_str[l])
                l += 1

            my_set.add(my_str[r])
            ans = max(ans, len(my_set))

        return ans


def full_pipeline(nums):

    sol = Solution()
    ans = sol.lengthOfLongestSubstring(nums)
    return ans

numbers = "abcabcbb"

print( full_pipeline(numbers) )


str_list = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )