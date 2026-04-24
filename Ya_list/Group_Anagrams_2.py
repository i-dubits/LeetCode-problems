
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_to_list = defaultdict(list)

        for word in strs:
            freq_arr = [0] * 26
            for curr_ch in word:
                freq_arr[ord(curr_ch) - ord('a')] += 1
            tuple_to_list[tuple(freq_arr)].append(word)

        ans = []
        for curr_list in tuple_to_list.values():
            ans.append(curr_list)

        return ans

def full_pipeline(nums):

    sol = Solution()
    ans = sol.groupAnagrams(*nums)
    return ans

numbers = [["eat","tea","tan","ate","nat","bat"]]
print( full_pipeline(numbers) )


str_list = [
    [["eat","tea","tan","ate","nat","bat"]],
    [[""]],
    [["a"]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )