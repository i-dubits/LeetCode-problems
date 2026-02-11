from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []

        ans = [0] * len(temperatures)

        if len(temperatures) == 1:
            return [0]

        temp_stack.append((0, temperatures[0]))
        for day in range(1, len(temperatures)):

            while temp_stack and temperatures[day] > temp_stack[-1][1]:
                prev_day, prev_temp = temp_stack[-1]
                ans[prev_day] = day - prev_day
                temp_stack.pop()

            else:
                temp_stack.append((day, temperatures[day]))

        return ans

def full_pipeline(numbers):
    sol = Solution()
    ans = sol.dailyTemperatures(numbers)
    # print(ans)
    return ans


numbers = [30,38,30,36,35,40,28]
print( full_pipeline(numbers) )


str_list = [
    [30,38,30,36,35,40,28],
    [22,21,20],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )