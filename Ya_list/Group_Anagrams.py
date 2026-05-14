
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_to_anagram = defaultdict(list)

        for word in strs:
            curr_tuple = self.make_tuple(word)
            tuple_to_anagram[curr_tuple].append(word)

        ans = []
        for curr_tuple, curr_list in tuple_to_anagram.items():
            ans.append(curr_list)

        return ans

    def make_tuple(self, source_str):
        freq_dict = defaultdict(int)
        for curr_char in source_str:
            freq_dict[curr_char] += 1

        res = []
        for key in sorted(freq_dict):
            res.append(key)
            res.append(freq_dict[key])

        res = tuple(res)
        return res

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