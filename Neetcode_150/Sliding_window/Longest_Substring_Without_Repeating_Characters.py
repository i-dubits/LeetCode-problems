

class Solution:
    def lengthOfLongestSubstring(self, my_str: str) -> int:
        if len(my_str) == 0:
            return 0

        ans = 0
        curr_l = 0
        l = 0
        curr_l = 0
        curr_chars = set()
        for r in range(len(my_str)):
            if my_str[r] not in curr_chars:
                curr_chars.add(my_str[r])
                curr_l = r - l + 1
                ans = max(ans, curr_l)

            else:
                while my_str[r] in curr_chars:
                    curr_chars.remove(my_str[l])
                    l += 1
                curr_chars.add(my_str[r])



        ans = max(ans, curr_l)
        return ans



def full_pipeline(numbers):
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(numbers)
    # print(ans)
    return ans


# numbers = "zxyzxyz"
# numbers = "abcabcbb"
numbers = "abba"
# numbers = "dvdf"

print( full_pipeline(numbers) )


str_list = [
    "zxyzxyz",
    "xxxx",
    "dvdf",
    "pwwkew",
    "abcabcbb",
    "abba",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )


