
from typing import Optional
from trees_utils import TreeNode, list_to_tree
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        loc_min, loc_max = -math.inf, math.inf

        ans = self.isValidRec(root, loc_min, loc_max)
        return ans

    def isValidRec(self, root, loc_min, loc_max):
        if root.val <= loc_min or root.val >= loc_max:
            return False

        if root.left is None and root.right is None:
            return True

        res_l, res_r = True, True
        if root.left is not None:
            res_l = self.isValidRec(root.left, loc_min, root.val)

        if root.right is not None:
            res_r = self.isValidRec(root.right, root.val, loc_max)

        return res_l and res_r



def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.isValidBST(tree)
    # print(res)
    return res


root = [2,1,3]
# root = [1,2,3]
print( full_pipeline(root) )


str_list = [
    [2,1,3],
    [1,2,3],
    [2,2,2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )