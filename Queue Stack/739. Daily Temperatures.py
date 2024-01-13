class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers = [0]*len(temperatures)
        self.my_stack = []

        self.my_stack.append([temperatures[0], 0])
        for i in range(1, len(temperatures)):
            while self.my_stack and self.my_stack[-1][0] < temperatures[i]:
                answers[self.my_stack.pop()[1]] = i
            self.my_stack.append([temperatures[i], i])

        answers = [answers[i] - i if answers[i] != 0 else 0 for i in range(len(answers))]

        return answers

# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
sol = Solution()
print(sol.dailyTemperatures((temperatures)))
