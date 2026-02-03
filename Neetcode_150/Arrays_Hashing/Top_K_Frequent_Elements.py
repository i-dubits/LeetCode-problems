from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_to_el = [ [] for _ in range(len(nums) + 1)]
        el_to_freq = defaultdict(int)

        for el in nums:
            el_to_freq[el] += 1

        for el, freq in el_to_freq.items():
            freq_to_el[freq].append(el)

        ans = []
        for curr_freq in range(len(nums), -1, -1):
            if len(ans) < k and len(freq_to_el[curr_freq]) != 0:
                ans.extend(freq_to_el[curr_freq])
            if len(ans) == k:
                return ans

        return ans



def full_pipeline(nums, k):
    sol = Solution()
    ans = sol.topKFrequent(nums, k)
    # print(ans)
    return ans

# print( full_pipeline([1,1,1,2,2,3], 2) )
print( full_pipeline([1,2,2,3,3,3], 2) )


str_list = [
    [[1,2,2,3,3,3], 2],
    [[7,7], 1],
    [[1,1,1,2,2,3], 2]
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )