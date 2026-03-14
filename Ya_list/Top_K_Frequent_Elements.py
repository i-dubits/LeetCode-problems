
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        freq_to_set = defaultdict(set)
        el_to_freq = defaultdict(int)
        freq_list_ordered = []

        for el in nums:
            el_to_freq[el] += 1
            freq_to_set[el_to_freq[el]].add(el)
            if el_to_freq[el] > max_freq:
                max_freq = el_to_freq[el]
                freq_list_ordered.append(el_to_freq[el])

        ans = set()
        for freq in reversed(freq_list_ordered):
            if len(ans) >= k:
                break
            for el in freq_to_set[freq]:
                if len(ans) < k:
                    ans.add(el)
                else:
                    break

        return list(ans)


def full_pipeline(nums):

    sol = Solution()
    ans = sol.topKFrequent(*nums)
    return ans

numbers = [[1,1,1,2,2,3], 2]

print( full_pipeline(numbers) )


str_list = [
    [[1,1,1,2,2,3], 2],
    [[1], 1],
    [[1,2,1,2,1,2,3,1,3,2], 2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )