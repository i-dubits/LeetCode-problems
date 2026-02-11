
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        source_dict = defaultdict(int)
        total_symb = 0
        for ch in s1:
            source_dict[ch] += 1
            total_symb += 1

        cnt_symbols_to_find = total_symb

        left = 0
        curr_source_dict = source_dict.copy()

        for right in range(len(s2)):
            curr_ch = s2[right]
            if curr_ch in curr_source_dict:
                if curr_source_dict[curr_ch] > 0:
                    curr_source_dict[curr_ch] -= 1
                    cnt_symbols_to_find -= 1

                    if cnt_symbols_to_find == 0:
                        return True

                elif curr_source_dict[curr_ch] == 0:
                    while left != right and curr_source_dict[curr_ch] == 0:
                        curr_source_dict[s2[left]] += 1
                        cnt_symbols_to_find += 1
                        left += 1

                    curr_source_dict[curr_ch] -= 1
                    cnt_symbols_to_find -= 1

            else:
                left = right
                cnt_symbols_to_find = total_symb
                curr_source_dict = source_dict.copy()

        if cnt_symbols_to_find == 0:
            return True
        else:
            return False



def full_pipeline(s1, s2):
    sol = Solution()
    ans = sol.checkInclusion(s1, s2)
    return ans


# str_inpt = ["abc", "lecabee"]
str_inpt = ["adc", "dcda"]

print( full_pipeline(*str_inpt) )


str_list = [
    ["abc", "lecabee"],
    ["abc", "lecaabee"],
    ["adc", "dcda"]
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )