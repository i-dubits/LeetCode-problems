from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_tuple_to_list = defaultdict(list)

        for curr_str in strs:
            freq_list = [0 for i in range(26)]
            for curr_char in curr_str:
                freq_list[ord(curr_char) - ord('a')] += 1
            freq_tuple = tuple(freq_list)
            freq_tuple_to_list[freq_tuple] += [curr_str]

        ans = []
        for str_list in freq_tuple_to_list.values():
                ans.append(str_list)

        return ans

def full_pipeline(str_curr):
    sol = Solution()
    ans = sol.groupAnagrams(str_curr)
    # print(ans)
    return ans

str_list = [
    ["act","pots","tops","cat","stop","hat"],
    ["x"],
    [""]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )