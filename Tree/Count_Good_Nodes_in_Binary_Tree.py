
from typing import Optional
from trees_utils import TreeNode, list_to_tree

import math

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.goodRec(root, -math.inf)

        return self.count

    def goodRec(self, root, branch_max):
        if root is None:
            return

        if root.val >= branch_max:
            self.count += 1
            branch_max = root.val

        self.goodRec(root.left, branch_max)
        self.goodRec(root.right, branch_max)

        return


def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.goodNodes(tree)
    # res.display()
    return res

root = [3,1,4,3,"null",1,5]
print( full_pipeline(root) )


str_list = [
    [3,1,4,3,"null",1,5],
    [3,3,"null",4,2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )