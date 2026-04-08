
from typing import Optional
from trees_utils import TreeNode, list_to_tree
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        loc_min = -math.inf
        loc_max = math.inf
        self.ans = True
        self.validRec(root, loc_min, loc_max)
        return self.ans

    def validRec(self, root: TreeNode, loc_min: int, loc_max: int):
        if root is None:
            return

        if loc_min < root.val < loc_max:
            self.validRec(root.left, loc_min, min(loc_max, root.val))
            self.validRec(root.right, max(loc_min, root.val), loc_max)
        else:
            self.ans = False
            return


def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.isValidBST(tree)
    # res.display()
    return res

root = [2,1,3]
print( full_pipeline(root) )


str_list = [
    [2,1,3],
    [5,1,4,"null","null",3,6],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )