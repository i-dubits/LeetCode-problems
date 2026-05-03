
from typing import List


class Solution:
    def reverseWords(self, source: str) -> str:
        source = source.strip().split()

        ans = []
        for word in reversed(source):
            ans.append(word)
        return ' '.join(ans)

def full_pipeline(nums):

    sol = Solution()
    ans = sol.reverseWords(*nums)
    return ans

# numbers = ["the sky is blue"]
numbers = ["  hello world  "]

print( full_pipeline(numbers) )


str_list = [
    ["the sky is blue"],
    ["  hello world  "],
    ["a good   example"],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )