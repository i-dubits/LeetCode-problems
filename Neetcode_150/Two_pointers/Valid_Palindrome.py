
import re


class Solution:
    def isPalindrome(self, my_str: str) -> bool:
        rx = re.compile('([&#!\',.:;?])')

        my_str = my_str.lower().replace(" ", "")
        my_str = rx.sub('', my_str)

        first = 0
        second = len(my_str) - 1

        ans = True
        while first < second:
            if my_str[first] == my_str[second]:
                first += 1
                second -= 1
                continue
            else:
                ans = False
                break

        return ans



def full_pipeline(my_str):
    sol = Solution()
    ans = sol.isPalindrome(my_str)
    # print(ans)
    return ans

# my_str = "Was it a car or a cat I saw?"
my_str = "aba"
print( full_pipeline(my_str) )


str_list = [
    "Was it a car or a cat I saw?",
    "tab a cat",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )