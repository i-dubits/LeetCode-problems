
from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, source: str) -> List[int]:
        pass



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