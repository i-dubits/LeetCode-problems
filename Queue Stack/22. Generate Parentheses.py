class Solution:

    def __init__(self):
        self.par_list = []

    def rec_gen(self, curr: str, numb_right_par: int):

        if len(curr) == self.n * 2:
            self.par_list.append(curr)
            return
        else:
            curr += '('
            numb_right_par += 1
            if len(curr) + numb_right_par == self.n * 2:
                while numb_right_par > 0:
                    curr += ')'
                    numb_right_par -= 1
                    if len(curr) == self.n * 2:
                        self.par_list.append(curr)
                        return
            self.rec_gen(curr, numb_right_par)
            while numb_right_par > 0:
                curr += ')'
                numb_right_par -= 1
                if len(curr) == self.n * 2:
                    self.par_list.append(curr)
                    return
                else:
                    self.rec_gen(curr, numb_right_par)

    def generateParenthesis(self, n: int) -> list[str]:
        self.n = n
        self.rec_gen('', 0)
        return self.par_list


n = 3
sol = Solution()

print(sol.generateParenthesis(n))
