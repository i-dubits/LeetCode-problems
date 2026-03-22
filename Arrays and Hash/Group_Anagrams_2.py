from typing import List
from collections import defaultdict




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        if len(strs) == 1:
            ans.append([strs[0]])
            return ans

        tuple_to_list_str = defaultdict(list)

        for word in strs:
            word_count = [0] * 26
            for ch in word:
                word_count[ord(ch) - ord('a')] += 1

            tuple_to_list_str[tuple(word_count)].append(word)

        ans = list(tuple_to_list_str.values())
        return ans



def full_pipeline(nums):
    sol = Solution()
    ans = sol.groupAnagrams(*nums)
    # print(ans)
    return ans

print( full_pipeline([["eat","tea","tan","ate","nat","bat"]]) )


str_list = [
    [["eat","tea","tan","ate","nat","bat"]],
    [[""]],
    [["a"]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )