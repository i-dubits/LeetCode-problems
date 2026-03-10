
from typing import List
from collections import defaultdict

class Solution:
    def characterReplacement(self, my_str: str, k: int) -> int:
        ans = 1
        max_ch_cnt = 0

        cnt_dict = defaultdict(int)

        l = 0
        for r in range(len(my_str)):
            cnt_dict[my_str[r]] += 1
            if cnt_dict[my_str[r]] > max_ch_cnt:
                max_ch = max(cnt_dict, key=lambda key: cnt_dict[key])
                max_ch_cnt = cnt_dict[max_ch]

            if r - l + 1 - max_ch_cnt <= k:
                ans = max(ans, r - l + 1)

            while l <= r and r - l + 1 - max_ch_cnt > k:
                if cnt_dict[my_str[l]] != 0:
                    cnt_dict[my_str[l]] -= 1
                    max_ch = max(cnt_dict, key=lambda key: cnt_dict[key])
                    max_ch_cnt = cnt_dict[max_ch]

                l += 1
        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.characterReplacement(*nums)
    return ans

# numbers = ["XYYX", 2]
# numbers = ["ABAA", 0]
numbers = ["BAAA", 0]
print( full_pipeline(numbers) )


str_list = [
    ["XYYX", 2],
    ["AAABABB", 1],
    ["ABAA", 0]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )