
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, source: str) -> List[int]:
        char_to_start_end = defaultdict(list)

        for ind in range(len(source)):
            curr_char = source[ind]
            if curr_char not in char_to_start_end:
                char_to_start_end[curr_char].extend([ind, ind])
            else:
                char_to_start_end[curr_char][1] = ind

        chars_sorted = sorted(char_to_start_end, key=lambda key: char_to_start_end[key])

        segm_list = []
        prev_segm = char_to_start_end[chars_sorted[0]]
        last_was_merged = None
        if len(chars_sorted) == 1:
            return [len(source)]
        for curr_char in chars_sorted[1:]:
            curr_segm = char_to_start_end[curr_char]

            b1, e1 = prev_segm[0], prev_segm[1]
            b2, e2 = curr_segm[0], curr_segm[1]
            if e1 >= b2 and e2 >= b1:
                prev_segm[0] = min(b1, b2)
                prev_segm[1] = max(e1, e2)
                last_was_merged = True
            else:
                segm_list.append(prev_segm.copy())
                prev_segm = curr_segm
                last_was_merged = False

        if last_was_merged:
            segm_list.append(prev_segm.copy())
        else:
            segm_list.append(curr_segm.copy())

        size_list = []
        for segm in segm_list:
            curr_size = segm[1] - segm[0] + 1
            size_list.append(curr_size)

        return size_list



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