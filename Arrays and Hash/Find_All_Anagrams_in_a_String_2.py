from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, source: str, ana: str) -> List[int]:
        freq_list_target = [0] * 26
        freq_list_curr = [0] * 26

        ans = []

        if len(ana) > len(source):
            return []

        for curr_ch in ana:
            freq_list_target[ord(curr_ch) - ord('a')] += 1

        for ind in range(len(ana)):
            freq_list_curr[ord(source[ind]) - ord('a')] += 1

        match = sum( 1 for first, second in zip(freq_list_target, freq_list_curr) if first == second)

        if match == 26:
            ans.append(0)

        l = 0
        for r in range(len(ana), len(source)):
            char_l_ind = ord(source[l]) - ord('a')
            if freq_list_curr[char_l_ind] > 0:
                if freq_list_curr[char_l_ind] == freq_list_target[char_l_ind]:
                    match -= 1

                freq_list_curr[char_l_ind] -= 1
                if freq_list_curr[char_l_ind] == freq_list_target[char_l_ind]:
                    match += 1

            char_r_ind = ord(source[r]) - ord('a')
            if freq_list_curr[char_r_ind] == freq_list_target[char_r_ind]:
                match -= 1
            freq_list_curr[char_r_ind] += 1
            if freq_list_curr[char_r_ind] == freq_list_target[char_r_ind]:
                match += 1

            l += 1
            if match == 26:
                ans.append(l)

        return ans



def full_pipeline(nums):
    sol = Solution()
    ans = sol.findAnagrams(*nums)
    # print(ans)
    return ans

print( full_pipeline(["cbaebabacd", "abc"]) )


str_list = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )