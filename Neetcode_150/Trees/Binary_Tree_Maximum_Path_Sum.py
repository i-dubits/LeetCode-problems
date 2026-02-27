
from typing import Optional
from trees_utils import TreeNode, list_to_tree

import math

class Solution:

    ans = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf
        self.maxPathAcc(root)
        return self.ans

    def maxPathAcc(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            self.ans = max(self.ans, root.val)
            return root.val

        res_l, res_r = -math.inf, -math.inf
        if root.left is not None:
            res_l = self.maxPathAcc(root.left)

        if root.right is not None:
            res_r = self.maxPathAcc(root.right)

        res_l_refined = self.find_opt(root, res_l)
        res_r_refined = self.find_opt(root, res_r)

        self.ans = max(self.ans, res_l_refined, res_r_refined,
                       res_l_refined + res_r_refined - root.val)

        return max(res_l_refined, res_r_refined)

    def find_opt(self, root, res_child) -> int:
        if root.val < 0:
            if res_child < root.val:
                return root.val
            else:
                return root.val + res_child
        else:
            if res_child < 0:
                return root.val
            else:
                return root.val + res_child


def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.maxPathSum(tree)
    return res


# root = [1,2,3]
root = [0]
print( full_pipeline(root) )


str_list = [
    [1,2,3],
    [-15, 10, 20, "null", "null", 15, 5, -5],
    [0]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )
