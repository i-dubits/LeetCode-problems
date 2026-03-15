
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, source: str) -> List[int]:
        ch_to_last_pos = defaultdict(int)

        for ind, curr_ch in enumerate(source):
            ch_to_last_pos[curr_ch] = ind

        ans = []
        curr_part_end_ind = 0
        beg_curr = 0
        for ind, curr_ch in enumerate(source):
            curr_ch_end = ch_to_last_pos[curr_ch]
            curr_part_end_ind = max(curr_part_end_ind, curr_ch_end)

            if curr_part_end_ind == ind:
                curr_len = curr_part_end_ind - beg_curr + 1
                ans.append(curr_len)
                beg_curr = ind + 1

        return ans



def full_pipeline(nums):

    sol = Solution()
    ans = sol.partitionLabels(*nums)
    return ans

numbers = ["ababcbacadefegdehijhklij"]

print( full_pipeline(numbers) )


str_list = [
    ["ababcbacadefegdehijhklij"],
    ["eccbbbbdec"],
    ["xyxxyzbzbbisl"],
    ["abcabc"],
    ["aaa"]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )