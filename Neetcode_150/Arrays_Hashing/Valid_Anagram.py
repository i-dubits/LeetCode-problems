
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = defaultdict(int)
        for char in s:
            my_dict[char] += 1

        for char in t:
            if char in my_dict:
                my_dict[char] -= 1
                if my_dict[char] == 0:
                    del my_dict[char]
            else:
                return False

        if my_dict:
           return False

        return True

def full_pipeline(str_1, str_2):
    sol = Solution()
    ans = sol.isAnagram(str_1, str_2)
    # print(ans)
    return ans

str_list = [[('racecar'), ('carrace')],
            [('jar'), ('jam')],
            [('xx'), ('x')]]

for str_pair in str_list:
    print(full_pipeline(*str_pair))