
from typing import Optional, List

from trees_utils import TreeNode, list_to_tree
import math
from collections import deque

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = math.inf
        my_two_el = deque()

        def in_order_trav(root: TreeNode):
            nonlocal min_diff
            nonlocal my_two_el
            if root is None:
                return
            in_order_trav(root.left)
            my_two_el.append(root.val)
            if len(my_two_el) == 2:
                diff_cand = abs(my_two_el[1] - my_two_el[0])
                min_diff = min(diff_cand, min_diff)
                my_two_el.popleft()
            in_order_trav(root.right)

        in_order_trav(root)

        return min_diff


def full_pipeline(p):
    sol = Solution()
    tree_list = p[0]
    tree = list_to_tree(tree_list)
    res = sol.minDiffInBST(tree)
    # res.display()
    return res

root = [[4,2,6,1,3]]
print( full_pipeline(root) )


str_list = [
    [[4,2,6,1,3]],
    [[1,0,48,"null","null",12,49]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )