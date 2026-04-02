
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDRec(root):
            if root is None:
                return 0

            d_l = maxDRec(root.left)
            d_r = maxDRec(root.right)

            return max(d_r, d_l) + 1

        max_d = maxDRec(root)
        return max_d




def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.maxDepth(tree)
    # res.display()
    return res

root = [3,9,20,"null","null",15,7]
print( full_pipeline(root) )


str_list = [
    [3,9,20,"null","null",15,7],
    [1,"null",2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )