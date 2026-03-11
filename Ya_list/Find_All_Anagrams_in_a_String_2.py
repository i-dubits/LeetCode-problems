
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, source: str, ana: str) -> List[int]:

        win_size = len(ana)
        ana_arr = [0]*26
        source_arr = [0]*26

        ans = []

        if win_size > len(source):
            return []

        for i in range(win_size):
            ch_ana = ana[i]
            ana_arr[ord(ch_ana) - ord('a')] += 1

            ch_source = source[i]
            source_arr[ord(ch_source) - ord('a')] += 1

        match_cnt = 0
        match_cnt = sum([1 for i in range(26) if ana_arr[i] == source_arr[i]])
        if match_cnt == 26:
            ans.append(0)

        l = 0
        for r in range(win_size, len(source)):
            ch_curr_l_ord = ord(source[l]) - ord('a')
            if source_arr[ch_curr_l_ord] == ana_arr[ch_curr_l_ord]:
                match_cnt -= 1
            source_arr[ch_curr_l_ord] -= 1
            if source_arr[ch_curr_l_ord] == ana_arr[ch_curr_l_ord]:
                match_cnt += 1
            l += 1

            ch_curr_r_ord = ord(source[r]) - ord('a')
            if source_arr[ch_curr_r_ord] == ana_arr[ch_curr_r_ord]:
                match_cnt -= 1
            source_arr[ch_curr_r_ord] += 1
            if source_arr[ch_curr_r_ord] == ana_arr[ch_curr_r_ord]:
                match_cnt += 1

            if match_cnt == 26:
                ans.append(l)


        return ans


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