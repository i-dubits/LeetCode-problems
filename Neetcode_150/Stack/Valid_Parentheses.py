
class Solution:
    def isValid(self, my_str: str) -> bool:
        my_stack = []
        for br in my_str:
            if br == '(' or br == '{' or br == '[':
                my_stack.append(br)
            else:
                if not my_stack:
                    return False
                cand = my_stack.pop()
                if br == ')' and cand != '(':
                    return False
                if br == '}' and cand != '{':
                    return False
                if br == ']' and cand != '[':
                    return False

        if my_stack:
            return False
        return True


def full_pipeline(numbers):
    sol = Solution()
    ans = sol.isValid(numbers)
    # print(ans)
    return ans


numbers = "[]"
print( full_pipeline(numbers) )


str_list = [
    "[]",
    "([{}])",
    "[(])",
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )