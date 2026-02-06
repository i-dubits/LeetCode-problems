
from collections import defaultdict

class Solution:
    def characterReplacement(self, str_init: str, k: int) -> int:
        l = 0
        ans = 0

        char_dict = defaultdict(int)
        for r in range(len(str_init)):
            char_dict[str_init[r]] += 1

            char_max, freq_max = self.get_freq_max(char_dict)
            while r - l + 1 - freq_max > k:
                char_dict[str_init[l]] -= 1
                l += 1
                char_max, freq_max = self.get_freq_max(char_dict)

            ans = max(ans, r - l + 1)
        return ans

    def get_freq_max(self, char_dict: dict):
        char_max = None
        freq_max = 0
        for ch, count in char_dict.items():
            if count > freq_max:
                freq_max = count
                char_max = ch

        return char_max, freq_max


def full_pipeline(s, k):
    sol = Solution()
    ans = sol.characterReplacement(s, k)
    # print(ans)
    return ans


# numbers = ["XYYX", 2]
# numbers = ["AAABABB", 1]
numbers = ["BAAA", 0]


print( full_pipeline(*numbers) )


str_list = [
    ["XYYX", 2],
    ["AAABABB", 1],
    ["BAAA", 0]
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )