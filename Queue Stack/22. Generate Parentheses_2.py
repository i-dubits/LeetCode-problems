
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                res.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        res = []
        backtrack()
        return res


n = 3
sol = Solution()

print(sol.generateParenthesis(n))