
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, source: str, ana: str) -> List[int]:

        ans = []
        ana_arr = [0]*26
        ana_total_cnt = 0
        win_size = len(ana)

        for ch in ana:
            ana_arr[ord(ch) - ord('a')] += 1
            ana_total_cnt += 1

        curr_arr = [0]*26
        l = 0
        for r in range(len(source)):
            curr_ch = source[r]
            curr_arr[ord(curr_ch) - ord('a')] += 1
            if r - l + 1 < win_size:
                continue
            elif r - l + 1 == win_size:
                if ana_arr == curr_arr:
                    ans.append(l)
            else:
                first_ch = source[l]
                curr_arr[ord(first_ch) - ord('a')] -= 1
                l += 1
                if ana_arr == curr_arr:
                    ans.append(l)

        return ans


    def create_window_dict(self, source, start, win_size, ana_dict):
        win_dict = defaultdict(int)

        for ind in range(start, start + win_size):
            curr_ch = source[ind]
            if curr_ch not in ana_dict:
                win_dict = None
                break
            else:
                win_dict[curr_ch] += 1

        return win_dict, ind + 1


def full_pipeline(nums):

    sol = Solution()
    ans = sol.findAnagrams(*nums)
    return ans

# numbers = ["cbaebabacd", "abc"]
numbers = ["abab", "ab"]
print( full_pipeline(numbers) )


str_list = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )